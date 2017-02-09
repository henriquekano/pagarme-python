from base_validators import check_existence, check_parameter_type, check_in_enum, check_max, check_min, check_max_length, check_min_length
from pagarme_lib_exception import PagarmeLibException

def check_api_key(func):
    def wrapper(parameters_list):
        check_existence('api_key', parameters_list)
        check_parameter_type('api_key', str, parameters_list)
        return func(parameters_list)
    return wrapper

def check_schema(schema):
    def function_wrapper(func):
        def parameters_wrapper(parameters_list):
            errors = []
            for key, constraints in schema.iteritems():
                if key in parameters_list:
                    if 'type' in constraints:
                        parameter_type = constraints['type']
                        error = check_parameter_type(key, parameter_type, parameters_list)
                        if error is not None: 
                            errors.append(error)
                    if 'required' in constraints:
                        error = check_existence(key, parameters_list)
                        if error is not None: 
                            errors.append(error)
                    if 'enum' in constraints:
                        enum_list = constraints['enum']
                        error = check_in_enum(key, enum_list, parameters_list)
                        if error is not None:
                            errors.append(error)
                    if 'max' in constraints:
                        max_value = constraints['max']
                        error = check_max(key, max_value, parameters_list)
                        if error is not None:
                            errors.append(error)
                    if 'min' in constraints:
                        min_value = constraints['min']
                        error = check_max(key, min_value, parameters_list)
                        if error is not None:
                            errors.append(error)
                    if 'max_length' in constraints:
                        max_length = constraints['max']
                        error = check_max_length(key, max_length, parameters_list)
                        if error is not None:
                            errors.append(error)
                    if 'min_length' in constraints:
                        min_length = constraints['min']
                        error = check_min_length(key, min_value, parameters_list)
                        if error is not None:
                            errors.append(error)
            if len(errors) > 0:
                raise PagarmeLibException(errors)
            else:
                a = func(parameters_list)
                return func(parameters_list)
        return parameters_wrapper
    return function_wrapper