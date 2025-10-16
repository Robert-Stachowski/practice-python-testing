
def is_valid_promo(code):
    if not isinstance(code, str):
        return False
    if len(code) != 10:
        return False
    if not all(char.isupper() or char.isdigit() for char in code):
        return False
    if sum (char.isdigit() for char in code) <2 :
        return False
    return True