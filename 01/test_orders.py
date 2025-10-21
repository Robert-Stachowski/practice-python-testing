import unittest, copy
from orders import validate_order

class TestValidateOrder(unittest.TestCase):
    def setUp(self):
        self.order = {
    "user_id": 101,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",         
        "address": "ul. Polna 10, 00-001 Warszawa"
      }
   }
       
    
    def test_validate_order_ok(self):
        result = validate_order(self.order)
        self.assertTrue(result)

    def test_invalid_dict_order(self):
        bad_order = None
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_dict_order_01(self):
        bad_order = " "
        with self.assertRaises(ValueError):
            validate_order(bad_order)



# user
    

    def test_invalid_user_id_string(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["user_id"] = "Niepoprawne dane :)"
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_missing_user_id(self):
        bad_order = copy.deepcopy(self.order)
        del bad_order["user_id"]
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_user_id_none(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["user_id"] = None
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_user_id_bool(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["user_id"] = True
        with self.assertRaises(ValueError):
            validate_order(bad_order)



# items  
    def test_invalid_items_epty_list(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["items"] = []
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_items_not_list(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["items"] = 1
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_missing_items(self):
        bad_order = copy.deepcopy(self.order)
        del bad_order["items"]
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_items_none(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["items"] = None
        with self.assertRaises(ValueError):
            validate_order(bad_order)

#delivery
    def test_invalid_delivery_empty_dict(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"] = {}
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_delivery_not_dict(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"] = "1a1"
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_missing_delivery(self):
        bad_order = copy.deepcopy(self.order)
        del bad_order["delivery"]
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_delivery_none(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"] = None
        with self.assertRaises(ValueError):
            validate_order(bad_order)

# method    
    def test_invalid_method_empty_string(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["method"] = ""
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_method_format(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["method"] = "1a1"
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_method_out_of_allowed_method(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["method"] = ("Poza zakresem dozwolonych metod")
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_missing_method_in_delivery(self):
        bad_order = copy.deepcopy(self.order)
        del bad_order["delivery"]["method"]
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_method_none(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["method"] = None
        with self.assertRaises(ValueError):
            validate_order(bad_order)


# address
    def test_invalid_address_not_string(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["address"] = 10101001
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_address_empty(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["address"] = " "
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_missing_address_in_delivery(self):
        bad_order = copy.deepcopy(self.order)
        del bad_order["delivery"]["address"]
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_address_none(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["address"] = None
        with self.assertRaises(ValueError):
            validate_order(bad_order)


    


if __name__ == "__main__":
    unittest.main()
