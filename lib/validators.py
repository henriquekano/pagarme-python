from base_validators import (
    check_existence,
    check_parameter_type,
    check_in_enum,
    check_max,
    check_min,
    check_max_length,
    check_min_length
)
from pagarme_lib_exception import PagarmeLibException


def _add_errors_to_list(errors_list, *args):
    """
    Args should be the errors individuals.
    Passing a list breaks the code.
    """
    errors = list(errors_list)
    for error in args:
        if error is not None:
            errors.append(error)
    return errors


def check_api_key(func):
    def wrapper(parameters_dict):
        errors = []
        errors = _add_errors_to_list(
            errors,
            check_existence('api_key', True, parameters_dict),
            check_parameter_type('api_key', str, parameters_dict)
        )
        if (len(errors) > 0):
            raise PagarmeLibException(errors)
        return func(parameters_dict)
    return wrapper


def _check_parameters_constraints(
        parameter_name, parameter_constraints, parameters_dict):
    errors = []
    if 'type' in parameter_constraints:
        parameter_type = parameter_constraints['type']
        errors = _add_errors_to_list(
            errors,
            check_parameter_type(
                parameter_name, parameter_type, parameters_dict)
        )
    if 'required' in parameter_constraints:
        errors = _add_errors_to_list(
            errors,
            check_existence(parameter_name, True, parameters_dict)
        )
    if 'enum' in parameter_constraints:
        enum_list = parameter_constraints['enum']
        errors = _add_errors_to_list(
            errors,
            check_in_enum(parameter_name, enum_list, parameters_dict)
        )
    if 'max' in parameter_constraints:
        max_value = parameter_constraints['max']
        errors = _add_errors_to_list(
            errors,
            check_max(parameter_name, max_value, parameters_dict)
        )
    if 'min' in parameter_constraints:
        min_value = parameter_constraints['min']
        errors = _add_errors_to_list(
            errors,
            check_min(parameter_name, min_value, parameters_dict)
        )
    if 'max_length' in parameter_constraints:
        max_length = parameter_constraints['max_length']
        errors = _add_errors_to_list(
            errors,
            check_max_length(parameter_name, max_length, parameters_dict)
        )
    if 'min_length' in parameter_constraints:
        min_length = parameter_constraints['min_length']
        errors = _add_errors_to_list(
            errors,
            check_min_length(parameter_name, min_length, parameters_dict)
        )
    if 'schema' in parameter_constraints:
        sub_schema = parameter_constraints['schema']
        sub_object = parameters_dict.get(parameter_name, {})
        return errors + _check_schema_recursive(sub_schema, sub_object)
    return errors

def _list_indexed_by_index(list_param):
    return {key: value for key, value in enumerate(list_param)}

def _check_special_constraints(parameter_name, constraints, parameters_dict):
    errors = []
    if 'all' in constraints:
        sub_schema = constraints.get('all')
        parameters_list = parameters_dict.get(parameter_name)
        parameters_list_indexed = _list_indexed_by_index(parameters_list)
        if parameters_list is not None:
            for index, item in enumerate(parameters_list):
                errors += _check_parameters_constraints(index, sub_schema, parameters_list_indexed)
    return errors


def _check_schema_recursive(schema, parameters_dict):
    errors = []
    for parameter_name, constraints in schema.items():
        name_in_parameters = parameter_name in parameters_dict
        required_parameter = 'required' in constraints
        if  name_in_parameters or required_parameter:
            errors += _check_parameters_constraints(
                parameter_name, constraints, parameters_dict)
            errors += _check_special_constraints(
                parameter_name, constraints, parameters_dict)
    return errors


def check_schema(schema_builder):
    def _function_wrapper(func):
        def _parameters_wrapper(parameters_dict):
            schema = schema_builder(parameters_dict)
            errors = _check_schema_recursive(schema, parameters_dict)
            if len(errors) > 0:
                raise PagarmeLibException(errors)
            else:
                return func(parameters_dict)
        return _parameters_wrapper
    return _function_wrapper
