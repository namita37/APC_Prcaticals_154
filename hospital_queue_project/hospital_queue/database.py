from datetime import datetime
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "hospital_queue.db"


def connect():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def initialize():
    with connect() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone TEXT NOT NULL DEFAULT '',
            department TEXT NOT NULL,
            doctor TEXT NOT NULL DEFAULT '',
            reason TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Waiting',
            registered_at TEXT NOT NULL,
            called_at TEXT
        )""")
        columns = {row["name"] for row in con.execute("PRAGMA table_info(patients)")}
        if "doctor" not in columns:
            con.execute("ALTER TABLE patients ADD COLUMN doctor TEXT NOT NULL DEFAULT ''")
        if "phone" not in columns:
            con.execute("ALTER TABLE patients ADD COLUMN phone TEXT NOT NULL DEFAULT ''")


def new_token(con):
    prefix = "Q" + datetime.now().strftime("%Y%m%d") + "-"
    row = con.execute("SELECT token FROM patients WHERE token LIKE ? ORDER BY id DESC LIMIT 1", (prefix + "%",)).fetchone()
    number = int(row["token"].split("-")[-1]) + 1 if row else 1
    return f"{prefix}{number:03d}"


def register_patient(name, age, phone, department, doctor, reason):
    with connect() as con:
        token = new_token(con)
        con.execute(
            "INSERT INTO patients(token,name,age,phone,department,doctor,reason,registered_at) VALUES(?,?,?,?,?,?,?,?)",
            (token, name, age, phone, department, doctor, reason, datetime.now().isoformat(timespec="minutes")),
        )
    return token


def get_patients():
    with connect() as con:
        return con.execute("SELECT token,name,age,phone,department,doctor,status,registered_at FROM patients ORDER BY id DESC").fetchall()


def get_patient_status(token):
    with connect() as con:
        patient = con.execute("SELECT id,token,name,department,doctor,status FROM patients WHERE token=?", (token,)).fetchone()
        if not patient:
            return None, 0
        ahead = con.execute(
            "SELECT COUNT(*) AS n FROM patients WHERE status='Waiting' AND department=? AND doctor=? AND id < ?",
            (patient["department"], patient["doctor"], patient["id"]),
        ).fetchone()["n"]
        return patient, ahead


def check_patient_login(token, phone):
    with connect() as con:
        return con.execute("SELECT token FROM patients WHERE token=? AND phone=?", (token, phone)).fetchone() is not None


def call_next():
    with connect() as con:
        row = con.execute("SELECT id,token,name,department FROM patients WHERE status='Waiting' ORDER BY id LIMIT 1").fetchone()
        if row:
            con.execute("UPDATE patients SET status='In Consultation',called_at=? WHERE id=?", (datetime.now().isoformat(timespec="minutes"), row["id"]))
        return row


def complete_patient(token):
    with connect() as con:
        cur = con.execute("UPDATE patients SET status='Completed' WHERE token=? AND status='In Consultation'", (token,))
        return cur.rowcount > 0


def dataframe_for_export():
    import pandas as pd
    with connect() as con:
        return pd.read_sql_query(
            "SELECT token AS 'Queue Token', name AS 'Patient', age AS 'Age', phone AS 'Phone', "
            "department AS 'Department', doctor AS 'Doctor', reason AS 'Reason', status AS 'Status', "
            "registered_at AS 'Registered At', called_at AS 'Called At' FROM patients ORDER BY id", con
        )


def dataframe_for_charts():
    import pandas as pd
    with connect() as con:
        return pd.read_sql_query("SELECT department,doctor FROM patients ORDER BY id", con)
