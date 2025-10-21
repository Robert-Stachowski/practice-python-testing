import pytest
from cart import Cart

@pytest.fixture
def empty_cart():
    cart = Cart()
    return cart

@pytest.fixture
def cart_with_items():
    cart = Cart()
    cart.add({"name": "apple", "price": 3.5})
    cart.add({"name": "banana", "price": 4})
    cart.add({"name": "kiwi", "price": 6.3})
    cart.add({"name": "apple", "price": 3.8})
    return cart



def test_add(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"name": "orange", "price": 8}
    cart_with_items.add(new_product)
    len_after = len(cart_with_items.items())
    assert len_after == len_before+1
    assert new_product in cart_with_items.items()

def test_add_none_name(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"name": None, "price": 8}    
    with pytest.raises(ValueError) as e:
        cart_with_items.add(new_product)
    len_after = len(cart_with_items.items())
    assert "Niepoprawny format" in str(e.value)
    assert len_after == len_before

def test_add_true_price(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"name": "peach", "price":False}    
    with pytest.raises(ValueError) as e:
        cart_with_items.add(new_product)
    len_after = len(cart_with_items.items())
    assert "niepoprawny format" in str(e.value)
    assert len_after == len_before

def test_add_true_name(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"name":True, "price":1}    
    with pytest.raises(ValueError) as e:
        cart_with_items.add(new_product)
    len_after = len(cart_with_items.items())
    assert "Niepoprawny format" in str(e.value)
    assert len_after == len_before

def test_add_none_price(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"name": "mango", "price": None}    
    with pytest.raises(ValueError) as e:
        cart_with_items.add(new_product)
    len_after = len(cart_with_items.items())
    assert "niepoprawny format" in str(e.value)
    assert len_after == len_before

def test_add_no_price(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"name": "mango"}    
    with pytest.raises(ValueError) as e:
        cart_with_items.add(new_product)
    len_after = len(cart_with_items.items())
    assert "brak pola cena" in str(e.value)
    assert len_after == len_before
    
def test_add_no_name(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"price": 8}    
    with pytest.raises(ValueError) as e:
        cart_with_items.add(new_product)
    len_after = len(cart_with_items.items())
    assert "Brak pola name" in str(e.value)
    assert len_after == len_before

def test_add_integer_name(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"name": 123, "price": 12}    
    with pytest.raises(ValueError) as e:
        cart_with_items.add(new_product)
    len_after = len(cart_with_items.items())
    assert "Niepoprawny format" in str(e.value)
    assert len_after == len_before

def test_add_string_price(cart_with_items):
    len_before = len(cart_with_items.items())
    new_product = {"name": "mango", "price": "dwa"}    
    with pytest.raises(ValueError) as e:
        cart_with_items.add(new_product)
    len_after = len(cart_with_items.items())
    assert "niepoprawny format" in str(e.value)
    assert len_after == len_before

def test_remove(cart_with_items):
    len_before = len(cart_with_items.items())
    cart_with_items.remove("apple")
    len_after = len(cart_with_items.items())
    assert len_after == len_before -1
    # porównanie stanu oczekiwanej listy do stanu faktycznego po usunięciu
    expected_names = {"banana","apple","kiwi"}
    names_after_remove = {p["name"] for p in cart_with_items.items()}
    assert names_after_remove == expected_names
    # liczenie ile "jabłek" zostało w koszyku. (były dwa pierwotnie)
    assert [p["name"] for p in cart_with_items.items()].count("apple") == 1

def test_remove_first_matching_product(cart_with_items):

    # sprawdzanie czy są dwa, oraz czy pierwsze wystąpienie się zgadza - cena 3.5
    apples_before = [p for p in cart_with_items.items() if p["name"] == "apple"]
    assert len(apples_before) == 2
    assert apples_before[0]["price"] == 3.5

    cart_with_items.remove("apple")

    # sprawdzanie po usunięciu, czy zostało usunięte pierwsze wystąpienie, porównując ceny (celowo różne dla poprawnego testu, aby móc rozróżnić)
    apple_after = [p for p in cart_with_items.items() if p["name"] == "apple"]
    assert len(apple_after) == 1
    assert apple_after[0]["price"] == 3.8


def test_total(cart_with_items):
    expected_total = 17.6
    result = cart_with_items.total()
    assert result == expected_total
    assert isinstance(result, float)


def test_empty_cart_total(empty_cart):
    expected_total = 0.0
    result = empty_cart.total()
    assert result == expected_total
    assert isinstance(result, float)


def test_remove_nonexistent_product(empty_cart):
    len_before = len(empty_cart.items())
    items_before = empty_cart.items()
    empty_cart.remove("egg")
    len_after = len(empty_cart.items())
    items_after = empty_cart.items()
    assert len_after == len_before
    assert items_before == items_after

def test_remove_nonexistent_product_ful_cart(cart_with_items):
    len_before = len(cart_with_items.items())
    items_before = cart_with_items.items()
    cart_with_items.remove("plum")
    len_after = len(cart_with_items.items())
    items_after = cart_with_items.items()
    assert len_before == len_after
    assert items_before == items_after


def test_items_deepcopy(cart_with_items):
    total_before = cart_with_items.total()
    copied_list = cart_with_items.items()
    copied_list[0]["price"] = 10
    total_after = cart_with_items.total()
    assert total_before == total_after
    assert copied_list is not cart_with_items.items()