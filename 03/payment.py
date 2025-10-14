
    
def send_payment(payment_data, gateway):
    try:
        result = gateway.pay(payment_data)
        return result is True
    except Exception:
        return False
