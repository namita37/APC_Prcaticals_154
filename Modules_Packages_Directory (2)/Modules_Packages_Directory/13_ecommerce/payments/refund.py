# payments/refund.py
from payments.process import _payment_records

def process_refund(order_id, reason=""):
    if order_id in _payment_records:
        _payment_records[order_id]["status"] = "Refunded"
        return f"Refund for {order_id} processed. Reason: {reason}"
    return f"No payment record for {order_id}."
