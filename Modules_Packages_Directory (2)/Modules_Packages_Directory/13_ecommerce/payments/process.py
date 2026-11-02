# payments/process.py
_payment_records = {}

def process_payment(order_id, customer_id, method="Cash"):
    _payment_records[order_id] = {"customer": customer_id, "method": method, "status": "Paid"}
    return f"Payment for {order_id} processed via {method}."
