def validate_user(data):
    
    if not isinstance(data,dict):
        return False
    
    required_keys = {"email","age","name"}
    if not required_keys.issubset(data):
        return False
    
    email = data.get("email")
    if not isinstance(email, str) or email != email.strip():
        return False
    if "@" not in email or not email.endswith((".pl", ".com")):
        return False
    
    age = data.get("age")
    if not isinstance(age, int) or age <18:
        return False
    
    name = data.get("name")
    if not isinstance(name, str) or name != name.strip():
        return False
    if not name.isalpha():
        return False
    
    return True
