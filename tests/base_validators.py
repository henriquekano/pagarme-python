import unittest
from lib.base_validators import (
        check_existence,
        check_parameter_type,
        check_in_enum,
        check_max,
        check_min,
        check_max_length,
        check_min_length
    )


class BaseValidators(unittest.TestCase):
    base_dictionary = {
        "str_parameter": "",
        "int_parameter": 1,
        "dict_parameter": {},
        "enum_parameter": "something"
    }

    def test_check_dict_key_existence_fail(self):
        key = "no_parameter"
        errors = check_existence(key, True, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)

    def test_check_dict_key_existence_success(self):
        key = "str_parameter"
        errors = check_existence(key, True, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)

    def test_check_parameter_type_fail(self):
        key = "str_parameter"
        parameter_type = int
        parameters_dictionary = BaseValidators.base_dictionary
        errors = check_parameter_type(
            key,
            parameter_type,
            parameters_dictionary
        )
        self.assertTrue(type(errors) is dict)

    def test_check_parameter_type_success(self):
        key = "str_parameter"
        parameter_type = str
        errors = check_parameter_type(
            key,
            parameter_type,
            BaseValidators.base_dictionary
        )
        self.assertTrue(errors is None)

    def test_check_in_enum_fail(self):
        key = "enum_parameter"
        enum = []
        errors = check_in_enum(key, enum, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)

    def test_check_in_enum_success(self):
        key = "enum_parameter"
        enum = [BaseValidators.base_dictionary[key]]
        errors = check_in_enum(key, enum, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)

    def test_check_max_fail(self):
        key = "int_parameter"
        max_value = BaseValidators.base_dictionary[key] - 1
        errors = check_max(key, max_value, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)
        max_value -= 1
        errors = check_max(key, max_value, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)

    def test_check_max_success(self):
        key = "int_parameter"
        max_value = BaseValidators.base_dictionary[key]
        errors = check_max(key, max_value, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)
        max_value += 1
        errors = check_max(key, max_value, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)

    def test_check_min_fail(self):
        key = "int_parameter"
        min_value = BaseValidators.base_dictionary[key] + 1
        errors = check_min(key, min_value, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)
        min_value += 1
        errors = check_min(key, min_value, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)

    def test_check_min_success(self):
        key = "int_parameter"
        min_value = BaseValidators.base_dictionary[key]
        errors = check_min(key, min_value, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)
        min_value -= 1
        errors = check_min(key, min_value, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)

    def test_check_max_length_fail(self):
        key = "str_parameter"
        length = len(BaseValidators.base_dictionary[key]) - 1
        errors = check_max_length(key, length, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)
        length -= 1
        errors = check_max_length(key, length, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)

    def test_check_max_length_success(self):
        key = "str_parameter"
        length = len(BaseValidators.base_dictionary[key])
        errors = check_max_length(key, length, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)
        length += 1
        errors = check_max_length(key, length, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)

    def test_check_min_length_fail(self):
        key = "str_parameter"
        length = len(BaseValidators.base_dictionary[key]) + 1
        errors = check_min_length(key, length, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)
        length += 1
        errors = check_min_length(key, length, BaseValidators.base_dictionary)
        self.assertTrue(type(errors) is dict)

    def test_check_min_length_success(self):
        key = "str_parameter"
        length = len(BaseValidators.base_dictionary[key])
        errors = check_min_length(key, length, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)
        length -= 1
        errors = check_min_length(key, length, BaseValidators.base_dictionary)
        self.assertTrue(errors is None)
