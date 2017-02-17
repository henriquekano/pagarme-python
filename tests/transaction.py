import unittest
from lib.transactions import transaction_create
from lib.pagarme_lib_exception import PagarmeLibException
from lib.configurations import PagarMeInit

class Validators(unittest.TestCase):

    def setUp(self):
        PagarMeInit('ak_test_zXjKL8u5uxn25HNxHviPbhthNV0nL7')

    def test_transaction_creation_fail(self):
        with self.assertRaises(Exception) as exception:
            transaction_create({})
        print exception.exception.value
        self.assertEquals(len(exception.exception.value), 7)

    def test_boleto_transaction_creation(self):
        with self.assertRaises(PagarmeLibException) as exception:
            transaction_create({
              "payment_method":"boleto",
              "amount": 122
            })
        print exception.exception.value