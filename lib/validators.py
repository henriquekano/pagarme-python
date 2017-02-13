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


def _check_special_constraints(command, command_parameters, parameters_dict):
    errors = []
    if command is 'or':
        for or_object in command_parameters:
            for parameter, constraints in or_object.items():
                error = _check_parameters_constraints(
                            parameter, constraints, parameters_dict)
                if len(error) <= 0:
                    errors = []
                    break
                else:
                    errors += error
    if command is 'if':
        for if_object in command_parameters:
            condition = if_object.get('condition')(parameters_dict)
            if condition:
                constraints = if_object.get('then')
                errors += _check_schema_recursive(constraints, parameters_dict)
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


def check_schema(schema):
    def function_wrapper(func):
        def parameters_wrapper(parameters_dict):
            errors = _check_schema_recursive(schema, parameters_dict)
            if len(errors) > 0:
                raise PagarmeLibException(errors)
            else:
                return func(parameters_dict)
        return parameters_wrapper
    return function_wrapper
