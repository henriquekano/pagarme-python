import unittest
from lib.response_formatter import format_datetimes
from datetime import datetime

class ResponseFormatter(unittest.TestCase):

    def test_datetime_formatter(self):
        datetime_dict = {
            'date_created': '2015-08-27T17:53:56.000Z',
            'date_updated': '2015-08-27T17:53:56.000Z',
            'boleto_expiration_date': '2015-08-27T17:53:56.000Z',
            'expiration_date': '2015-08-27T17:53:56.000Z',
            'expiration_date': '1220',
            'sub_object': {
                'date_created': '2015-08-27T17:53:56.000Z',
                'date_updated': '2015-08-27T17:53:56.000Z',
                'boleto_expiration_date': '2015-08-27T17:53:56.000Z',
                'expiration_date': '2015-08-27T17:53:56.000Z',
                'expiration_date': '1220'
            }
        }
        formatted = format_datetimes(lambda x: x)(datetime_dict)
        self.assertTrue(type(datetime_dict.get('date_created')) is datetime)
        self.assertTrue(type(datetime_dict.get('date_updated')) is datetime)
        self.assertTrue(type(datetime_dict.get('boleto_expiration_date')) is datetime)
        self.assertTrue(type(datetime_dict.get('expiration_date')) is datetime)
        self.assertTrue(type(datetime_dict.get('expiration_date')) is datetime)
        self.assertTrue(type(datetime_dict.get('sub_object').get('date_created')) is datetime)
        self.assertTrue(type(datetime_dict.get('sub_object').get('date_updated')) is datetime)
        self.assertTrue(type(datetime_dict.get('sub_object').get('boleto_expiration_date')) is datetime)
        self.assertTrue(type(datetime_dict.get('sub_object').get('expiration_date')) is datetime)
        self.assertTrue(type(datetime_dict.get('sub_object').get('expiration_date')) is datetime)
