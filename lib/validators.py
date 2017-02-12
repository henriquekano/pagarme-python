from base_validators import check_existence, check_parameter_type, check_in_enum, check_max, check_min, check_max_length, check_min_length
from pagarme_lib_exception import PagarmeLibException

def check_api_key(func):
    def wrapper(parameters_list):
        check_existence('api_key', parameters_list)
        check_parameter_type('api_key', str, parameters_list)
        return func(parameters_list)
    return wrapper

def check_parameters_constraints(parameter_name, parameter_constraints, schema, parameters_list):
    errors = []
    if 'type' in parameter_constraints:
        parameter_type = parameter_constraints['type']
        error = check_parameter_type(parameter_name, parameter_type, parameters_list)
        if error is not None: 
            errors.append(error)
    if 'required' in parameter_constraints:
        error = check_existence(parameter_name, parameters_list)
        if error is not None: 
            errors.append(error)
    if 'enum' in parameter_constraints:
        enum_list = parameter_constraints['enum']
        error = check_in_enum(parameter_name, enum_list, parameters_list)
        if error is not None:
            errors.append(error)
    if 'max' in parameter_constraints:
        max_value = parameter_constraints['max']
        error = check_max(parameter_name, max_value, parameters_list)
        if error is not None:
            errors.append(error)
    if 'min' in parameter_constraints:
        min_value = parameter_constraints['min']
        error = check_max(parameter_name, min_value, parameters_list)
        if error is not None:
            errors.append(error)
    if 'max_length' in parameter_constraints:
        max_length = parameter_constraints['max']
        error = check_max_length(parameter_name, max_length, parameters_list)
        if error is not None:
            errors.append(error)
    if 'min_length' in parameter_constraints:
        min_length = parameter_constraints['min']
        error = check_min_length(parameter_name, min_length, parameters_list)
        if error is not None:
            errors.append(error)
    return errors

def check_special_constraints():
    return []

def check_schema_recursive(schema, parameters_list):
    errors = []
    for parameter_name, constraints in schema.iteritems():
        if parameter_name in parameters_list:
            errors = check_parameters_constraints(parameter_name, constraints, schema, parameters_list)
            #check sub schemas
            if 'schema' in constraints:
                sub_schema = constraints['schema']
                sub_object = parameters_list.get(parameter_name, {})
                return check_schema_recursive(sub_schema, sub_object) + errors
        else:
            errors += check_special_constraints()
    return errors

def check_schema(schema):
    def function_wrapper(func):
        def parameters_wrapper(parameters_list):
            errors = check_schema_recursive(schema, parameters_list)
            if len(errors) > 0:
                raise PagarmeLibException(errors)
            else:
                return func(parameters_list)
        return parameters_wrapper
    return function_wrapper