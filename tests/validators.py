import unittest
from lib.validators import (
    check_api_key, _check_parameters_constraints
)
from lib.pagarme_lib_exception import PagarmeLibException


class Validators(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Validators, self).__init__(*args, **kwargs)
        self.decorated_check_api_key = check_api_key(lambda *args: args)

    def test_check_api_key_existence_fail(self):
        with self.assertRaises(PagarmeLibException) as exception:
            parameters = {
                'not_api_key': ''
            }
            errors = self.decorated_check_api_key(parameters)
        self.assertTrue(len(exception.exception.value) > 0)

    def test_check_api_key_format_fail(self):
        with self.assertRaises(PagarmeLibException) as exception:
            parameters = {
                'api_key': 0
            }
            errors = self.decorated_check_api_key(parameters)
        self.assertTrue(len(exception.exception.value) > 0)

    def test_check_api_key_success(self):
        parameters = {
            'api_key': 'UMA API KEY'
        }
        errors = self.decorated_check_api_key(parameters)
        # assert it doesnt raises an exception

    def test_check_schema_type_constraint_fail(self):
        schema = {
            'parameter': {
                'type': str
            }
        }
        parameters_dict = {
            'parameter': 1
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 1)

    def test_check_schema_type_constraint_success(self):
        schema = {
            'parameter': {
                'type': str
            }
        }
        parameters_dict = {
            'parameter': ''
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_required_constraint_fail(self):
        schema = {
            'parameter': {
                'required': str
            }
        }
        parameters_dict = {
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 1)

    def test_check_schema_required_constraint_success(self):
        schema = {
            'parameter': {
                'required': str
            }
        }
        parameters_dict = {
            'parameter': None
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_enum_constraint_fail(self):
        schema = {
            'parameter': {
                'enum': ['something']
            }
        }
        parameters_dict = {
            'parameter': 'Not something'
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 1)

    def test_check_schema_enum_constraint_success(self):
        schema = {
            'parameter': {
                'enum': ['something']
            }
        }
        parameters_dict = {
            'parameter': 'something'
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_max_constraint_fail(self):
        schema = {
            'parameter': {
                'max': 5
            }
        }
        parameters_dict = {
            'parameter': 6
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 1)

    def test_check_schema_max_equals_constraint_success(self):
        schema = {
            'parameter': {
                'max': 5
            }
        }
        parameters_dict = {
            'parameter': 5
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_max_constraint_success(self):
        schema = {
            'parameter': {
                'max': 5
            }
        }
        parameters_dict = {
            'parameter': 4
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_min_constraint_fail(self):
        schema = {
            'parameter': {
                'min': 5
            }
        }
        parameters_dict = {
            'parameter': 4
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 1)

    def test_check_schema_min_equals_constraint_success(self):
        schema = {
            'parameter': {
                'min': 5
            }
        }
        parameters_dict = {
            'parameter': 5
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_min_constraint_success(self):
        schema = {
            'parameter': {
                'min': 5
            }
        }
        parameters_dict = {
            'parameter': 6
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_min_length_constraint_fail(self):
        schema = {
            'parameter': {
                'min_length': 5
            }
        }
        parameters_dict = {
            'parameter': '1234'
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 1)

    def test_check_schema_min_length_equals_constraint_success(self):
        schema = {
            'parameter': {
                'min_length': 5
            }
        }
        parameters_dict = {
            'parameter': '12345'
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_min_length_constraint_success(self):
        schema = {
            'parameter': {
                'min_length': 5
            }
        }
        parameters_dict = {
            'parameter': '123456'
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_max_length_constraint_fail(self):
        schema = {
            'parameter': {
                'max_length': 5
            }
        }
        parameters_dict = {
            'parameter': '123456'
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 1)

    def test_check_schema_max_length_equals_constraint_success(self):
        schema = {
            'parameter': {
                'max_length': 5
            }
        }
        parameters_dict = {
            'parameter': '12345'
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)

    def test_check_schema_max_length_constraint_success(self):
        schema = {
            'parameter': {
                'max_length': 5
            }
        }
        parameters_dict = {
            'parameter': '1234'
        }
        constraint = schema['parameter']
        errors = _check_parameters_constraints(
            'parameter',
            constraint,
            parameters_dict
        )
        self.assertTrue(type(errors) is list)
        self.assertEquals(len(errors), 0)
