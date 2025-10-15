def validate_user(data):
    email = data.get("email","")
    if "@" not in email or not data.get("email").endswith((".pl", ".com")):
        return False
    age = data.get("age")
    if not isinstance(age, int) or age <18:
        return False
    name = data.get("name","")
    if not name.isalpha():
        return False
    return True
