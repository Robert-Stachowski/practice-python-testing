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

    def test_invalid_user_id(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["user_id"] = "Niepoprawne dane :)"
        with self.assertRaises(ValueError):
            validate_order(bad_order)
    
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
    
    def test_invalid_method_empty_set(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["method"] = set()
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_method_not_dict(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["method"] = "1a1"
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_method_out_of_allowed_method(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["method"] = ("Poza zakresem dozwolonych metod"," i druga do pary")
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_address_not_string(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["address"] = 10101001
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    def test_invalid_address_empty(self):
        bad_order = copy.deepcopy(self.order)
        bad_order["delivery"]["address"] = ""
        with self.assertRaises(ValueError):
            validate_order(bad_order)

    #def test_fields_none_raise_valueerror(self):
        
    #    bad_type = [
    #        ("user_id", None),
    #        ("items", None),
    #        ("delivery", None),
    #        ("delivery","method", None),
    #        ("delivery", "address", None)
     #       ]

        
            





if __name__ == "__main__":
    unittest.main()
