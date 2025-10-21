def validate_order(order):

    if not isinstance(order, dict):
        raise ValueError("Błąd danych")
    
    user_id = order.get("user_id")
    if not isinstance(user_id, int) or isinstance(user_id,bool):
        raise ValueError("Nieprawidłowy user_id")
    
    items = order.get("items")
    if not isinstance(items, list) or len(items)==0:
        raise ValueError("Lista pusta")
    
    delivery = order.get("delivery")
    if not isinstance(delivery, dict):
        raise ValueError("niepoprawny format")
    
    allowed_method = ("courier", "pickup", "drone")
    delivery_methods = delivery.get("method")
    if delivery_methods not in allowed_method:
        raise ValueError(" Nieprawidłowa metoda")
    
    delivery_address = delivery.get("address")
    if not isinstance(delivery_address, str) or not delivery_address.strip():
        raise ValueError("Brak lub nieprawidłowy adres")

    return True
