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
    assert new_product in cart_with_items.items()
    

def test_remove_product(cart_with_items):
    len_before = len(cart_with_items.items())
    cart_with_items.remove_product("apple")
    len_after = len(cart_with_items.items())
    assert len_after == len_before -1
    # porównanie stanu oczekiwanej listy do stanu faktycznego po usunięciu
    expected_names = {"banana","apple","kiwi"}
    names_after_remove = {p["name"] for p in cart_with_items.items()}
    assert names_after_remove == expected_names
    # liczenie ile "jabłek" zostało w koszyku. (były dwa pierwotnie)
    assert [p["name"] for p in cart_with_items.items()].count("apple") == 1


def test_total_price(cart_with_items):
    expected_total = 17.6
    result = cart_with_items.total_price()
    assert result == expected_total
    assert isinstance(result, float)


def test_empty_cart_total(empty_cart):
    expected_total = 0.0
    result = empty_cart.total_price()
    assert result == expected_total
    assert isinstance(result, float)


def test_remove_nonexistent_product(empty_cart):
    len_before = len(empty_cart.items())
    items_before = empty_cart.items()
    empty_cart.remove_product("egg")
    len_after = len(empty_cart.items())
    items_after = empty_cart.items()
    assert len_after == len_before
    assert items_before == items_after

def test_remove_nonexistent_product_ful_cart(cart_with_items):
    len_before = len(cart_with_items.items())
    items_before = cart_with_items.items()
    cart_with_items.remove_product("plum")
    len_after = len(cart_with_items.items())
    items_after = cart_with_items.items()
    assert len_before == len_after
    assert items_before == items_after


def test_items_deepcopy(cart_with_items):
    total_before = cart_with_items.total_price()
    copied_list = cart_with_items.items()
    copied_list[0]["price"] = 10
    total_after = cart_with_items.total_price()
    assert total_before == total_after
    assert copied_list is not cart_with_items.items()