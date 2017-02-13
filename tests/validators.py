import unittest
from lib.validators import (
    check_api_key, _check_parameters_constraints, check_schema
)
from lib.pagarme_lib_exception import PagarmeLibException


class Validators(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Validators, self).__init__(*args, **kwargs)
        self.decorated_check_api_key = check_api_key(lambda *args: args)

    def test_check_schema_with_empty_dict(self):
        with self.assertRaises(PagarmeLibException) as exception:
            schema = {
                'parameter1': {
                    'type': str,
                    'required': True,
                    'max_length': 5
                }
            }
            parameters_dict = {}
            check_schema(schema)(lambda *args: args)(parameters_dict)
        self.assertEquals(type(exception.exception.value), list)
        self.assertEquals(len(exception.exception.value), 3)

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

    def test_check_multiple_parameters_fail(self):
        with self.assertRaises(PagarmeLibException) as exception:
            schema = {
                'parameter1': {
                    'max_length': 5
                },
                'parameter2': {
                    'type': str
                }
            }
            parameters_dict = {
                'parameter1': '123456',
                'parameter2': 0
            }
            check_schema(schema)(lambda *args: args)(parameters_dict)
        self.assertEquals(type(exception.exception.value), list)
        self.assertEquals(len(exception.exception.value), 2)

    def test_check_sub_schema_fail(self):
        with self.assertRaises(PagarmeLibException) as exception:
            schema = {
                'parameter': {
                    'schema': {
                        'sub_parameter': {
                            'schema': {
                                'sub_sub_parameter': {
                                    'max': 5,
                                    'type': int,
                                    'enum': [1, 2]
                                }
                            }
                        }
                    }
                }
            }
            parameters_dict = {
                'parameter': {
                    'sub_parameter': {
                        'sub_sub_parameter': 'ola'
                    }
                }
            }
            check_schema(schema)(lambda *args: args)(parameters_dict)
        self.assertTrue(type(exception.exception.value), list)
        self.assertEquals(len(exception.exception.value), 3)

    def test_check_sub_schema_success(self):
        schema = {
            'parameter': {
                'schema': {
                    'sub_parameter': {
                        'schema': {
                            'sub_sub_parameter': {
                                'max': 5,
                                'type': int,
                                'enum': [1, 2]
                            }
                        }
                    }
                }
            }
        }
        parameters_dict = {
            'parameter': {
                'sub_parameter': {
                    'sub_sub_parameter': 2
                }
            }
        }
        check_schema(schema)(lambda *args: args)(parameters_dict)
        # assert doesnt raises exceptions

    def test_or_command_both_fail(self):
        with self.assertRaises(PagarmeLibException) as exception:
            schema = {
                'or': [
                    {
                        'parameter1': {
                            'type': str
                        },
                        'parameter2': {
                            'type': int
                        }
                    }
                ]
            }
            parameters_dict = {
                'parameter1': 0,
                'parameter2': ''
            }
            check_schema(schema)(lambda *args: args)(parameters_dict)
        self.assertEquals(type(exception.exception.value), list)
        self.assertEquals(len(exception.exception.value), 2)

    def test_or_command_one_success(self):
        schema = {
            'or': [
                {
                    'parameter1': {
                        'type': str
                    },
                    'parameter2': {
                        'type': int
                    }
                }
            ]
        }
        parameters_dict = {
            'parameter1': ''
        }
        check_schema(schema)(lambda *args: args)(parameters_dict)
        # assert doesnt raises exceptions

    def test_or_command_other_success(self):
        schema = {
            'or': [
                {
                    'parameter1': {
                        'type': str
                    },
                    'parameter2': {
                        'type': int
                    }
                }
            ]
        }
        parameters_dict = {
            'parameter2': 0
        }
        check_schema(schema)(lambda *args: args)(parameters_dict)
        # assert doesnt raises exceptions

    def test_or_command_both_success(self):
        schema = {
            'or': [
                {
                    'parameter1': {
                        'type': str
                    },
                    'parameter2': {
                        'type': int
                    }
                }
            ]
        }
        parameters_dict = {
            'parameter1': '',
            'parameter2': 0
        }
        check_schema(schema)(lambda *args: args)(parameters_dict)
        # assert doesnt raises exceptions

    def test_if_command_success(self):
        with self.assertRaises(PagarmeLibException) as exception:
            schema = {
                'if': [
                    {
                        'condition':
                            lambda parameters_dict:
                                parameters_dict.get('parameter1') is True
                        ,'then': {
                            'parameter2': {
                                'type': int
                            }
                        }
                    }
                ]
            }
            parameters_dict = {
                'parameter1': True,
                'parameter2': ''
            }
            check_schema(schema)(lambda *args: args)(parameters_dict)
        self.assertTrue(type(exception.exception.value) is list)
        self.assertEquals(len(exception.exception.value), 1)

    def test_if_command_fail(self):
        schema = {
            'if': [
                {
                    'condition':
                        lambda parameters_dict:
                            parameters_dict.get('parameter1') is True
                    ,'then': {
                        'parameter2': {
                            'type': int
                        }
                    }
                }
            ]
        }
        parameters_dict = {
            'parameter1': False,
            'parameter2': ''
        }
        check_schema(schema)(lambda *args: args)(parameters_dict)
        # assert doesnt raises exceptions
    
    def test_or_nested_if_command_fail(self):
        with self.assertRaises(PagarmeLibException) as exception:
            schema = {
                'if': [
                    {
                        'condition':
                            lambda parameters_dict:
                                parameters_dict.get('parameter1') is True
                        ,'then': {
                            'or': [
                                {
                                    'parameter2': {
                                        'type': int
                                    },
                                    'parameter3': {
                                        'type': int
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
            parameters_dict = {
                'parameter1': True,
                'parameter2': '',
                'parameter3': ''
            }
            check_schema(schema)(lambda *args: args)(parameters_dict)
        self.assertTrue(type(exception.exception.value) is list)
        self.assertEquals(len(exception.exception.value), 2)

    def test_or_nested_if_command_one_success(self):
        schema = {
            'if': [
                {
                    'condition':
                        lambda parameters_dict:
                            parameters_dict.get('parameter1') is True
                    ,'then': {
                        'or': [
                            {
                                'parameter2': {
                                    'type': int
                                },
                                'parameter3': {
                                    'type': int
                                }
                            }
                        ]
                    }
                }
            ]
        }
        parameters_dict = {
            'parameter1': True,
            'parameter2': 0,
            'parameter3': ''
        }
        check_schema(schema)(lambda *args: args)(parameters_dict)
        # assert doesnt raises exceptions

    def test_or_nested_if_command_other_success(self):
        schema = {
            'if': [
                {
                    'condition':
                        lambda parameters_dict:
                            parameters_dict.get('parameter1') is True
                    ,'then': {
                        'or': [
                            {
                                'parameter2': {
                                    'type': int
                                },
                                'parameter3': {
                                    'type': int
                                }
                            }
                        ]
                    }
                }
            ]
        }
        parameters_dict = {
            'parameter1': True,
            'parameter2': '',
            'parameter3': 0
        }
        check_schema(schema)(lambda *args: args)(parameters_dict)
        # assert doesnt raises exceptions
