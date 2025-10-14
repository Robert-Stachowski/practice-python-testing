import unittest
from unittest.mock import Mock
from payment import send_payment

class Test_send_payment(unittest.TestCase):
   def test_successful_payment(self):
      payment_data = {"amount": 100, "currency": "PLN"}
      getaway = Mock()
      getaway.pay.return_value = True
      result = send_payment(payment_data, getaway)
      self.assertEqual(result, True)
      getaway.pay.assert_called_once_with(payment_data)
# weryfikacja czy funkcja wywoła pay() z własciwymi danymi

   def test_payment_failure(self):
      payment_data = {"amount": -100, "currency": "PLN"}
      getaway = Mock()
      getaway.pay.return_value = False
      result = send_payment(payment_data, getaway)
      self.assertEqual(result, False)
      getaway.pay.assert_called_once_with(payment_data)


   def test_payment_fails_when_gateway_raises_exception(self):
      payment_data = {"amount": -100, "currency": "PLN"}
      getaway = Mock()
      getaway.pay.side_effect = Exception("Error")
      result = send_payment(payment_data, getaway)
      self.assertEqual(result, False)
      getaway.pay.assert_called_once_with(payment_data)