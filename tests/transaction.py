import unittest
from lib.transactions import (
    transaction_create,
    transaction_capture,
    transaction_refund
)
from lib.pagarme_lib_exception import PagarmeLibException
from lib.configurations import PagarMeInit

class Transaction(unittest.TestCase):

    def setUp(self):
        PagarMeInit('ak_test_zXjKL8u5uxn25HNxHviPbhthNV0nL7')

    def test_transaction_creation_fail(self):
        with self.assertRaises(Exception) as exception:
            transaction_create({})
        self.assertEquals(len(exception.exception.value), 7)

    def test_boleto_transaction_creation(self):
        transaction_create({
          'payment_method':'boleto',
          'amount': 122
        })
        # assert it doesnt raise an exception

    # def test_splitted_boleto_transaction_creation(self):

    def test_credit_card_transaction_creation(self):
        created_transaction = transaction_create({
            'card_number': '4242424242424242',
            'card_cvv': '122',
            'card_holder_name': 'SDFSDF',
            'card_expiration_date': '1220',
            'customer':{
                'email':'email.do.cliente@gmail.com',
                'name':'nome',
                'document_number':'334.863.289-72',
                'address':{
                    'zipcode':'70631-035',
                    'neighborhood':'bairro',
                    'street':'rua',
                    'street_number':'122'
                },
                'phone': {
                    'number':'87654321',
                    'ddd':'11'
                }
            },
            'payment_method':'credit_card',
            'amount': 122
        })
        self.assertIsNotNone(created_transaction.get('id'))
        # assert it doesnt raise an exception

    # def test_splitted_credit_card_transaction_creation(self):

    def test_capture_transaction(self):
        created_transaction = transaction_create({
            'card_number': '4242424242424242',
            'card_cvv': '122',
            'card_holder_name': 'SDFSDF',
            'card_expiration_date': '1220',
            'capture': False,
            'customer':{
                'email':'email.do.cliente@gmail.com',
                'name':'nome',
                'document_number':'334.863.289-72',
                'address':{
                    'zipcode':'70631-035',
                    'neighborhood':'bairro',
                    'street':'rua',
                    'street_number':'122'
                },
                'phone': {
                    'number':'87654321',
                    'ddd':'11'
                }
            },
            'payment_method':'credit_card',
            'amount': 122
        })
        self.assertEquals(created_transaction.get('status'), 'authorized')
        created_transaction = transaction_capture(transaction=created_transaction)
        self.assertEquals(created_transaction.get('status'), 'paid')

    def test_transaction_refund(self):
        created_transaction = transaction_create({
            'card_number': '4242424242424242',
            'card_cvv': '122',
            'card_holder_name': 'SDFSDF',
            'card_expiration_date': '1220',
            'customer':{
                'email':'email.do.cliente@gmail.com',
                'name':'nome',
                'document_number':'334.863.289-72',
                'address':{
                    'zipcode':'70631-035',
                    'neighborhood':'bairro',
                    'street':'rua',
                    'street_number':'122'
                },
                'phone': {
                    'number':'87654321',
                    'ddd':'11'
                }
            },
            'payment_method':'credit_card',
            'amount': 122
        })
        refunded_transaction = transaction_refund(transaction=created_transaction)
        self.assertEquals(refunded_transaction.get('status'), 'refunded')
    # def test_capture_with_split_rules(self):

    # def test_capture_with_metadata(self):

    # def test_find_transaction(self):

    # def test_find_transaction_list(self):

    # def test_find_transaction_list_with_filters(self):

    # def test_find_payables(self):

    # def test_find_payable_list(self):

    

    # def test_partial_refund(self):