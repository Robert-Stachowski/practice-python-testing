import pytest
from cart import Cart

@pytest.fixture
def empty_cart():
    cart = Cart()
    return cart

@pytest.fixture
def cart_with_items():
    cart = Cart()
    cart.add_product({"name": "apple", "price": 3.5})
    cart.add_product({"name": "banana", "price": 4})
    cart.add_product({"name": "kiwi", "price": 6.3})
    cart.add_product({"name": "apple", "price": 3.8})
    return cart

def test_add_product(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"name": "orange", "price": 8}
    cart_with_items.add_product(new_product)
    len_after = len(cart_with_items.items())
    assert len_after == len_before+1


def test_remove_product(cart_with_items):
    len_before = len(cart_with_items.items())
    cart_with_items.remove_product("apple")
    len_after = len(cart_with_items.items())
    assert len_after == len_before -1
    # porównanie stanu oczekiwanej listy do stanu faktycznego po usunięciu
    expected_names = {"banana","apple","kiwi"}
    names_after_remove = {p["name"] for p in cart_with_items.items()}
    assert names_after_remove == expected_names
    

def test_total_price(cart_with_items):
    pass

def test_empty_cart_total(empty_cart):
    pass

def test_remove_nonexistent_product(empty_cart):
    pass