def check_existence(parameter, parameters_list):
    if(parameter not in parameters_list):
        return {
            'parameter': parameter,
            'type': 'existence',
            'message': (parameter + ' should exist')  
        }

def check_parameter_type(parameter, parameter_type, parameters_list):
    if(type(parameters_list.get(parameter)) is not parameter_type):
        return {
            'parameter': parameter,
            'type': 'format',
            'message': (parameter + ' should be a ' + str(parameter_type))
        }

def check_in_enum(parameter, parameter_enum, parameters_list):
    if(parameters_list.get(parameter) not in parameter_enum):
        return {
            'parameter': parameter,
            'type': 'format',
            'message': (parameter + ' should be one of: [' + ','.join(parameter_enum) + ']')
        }

def check_max(parameter, max_value, parameters_list):
    if(parameters_list.get(parameter) > max_value):
        return {
            'parameter': parameter,
            'type': 'format',
            'message': (parameter + ' should be at most ' + str(max_value))
        }

def check_min(parameter, min_value, parameters_list):
    if(parameters_list.get(parameter) < min_value):
        return {
            'parameter': parameter,
            'type': 'format',
            'message': (parameter + ' should be at minimum ' + str(min_value))
        }

def check_max_length(parameter, max_length, parameters_list):
    if(len(parameters_list.get(parameter)) > max_length):
        return {
            'parameter': parameter,
            'type': 'format',
            'message': (parameter + ' should be at most ' + str(max_length) + ' characters long')
        }

def check_min_length(parameter, min_length, parameters_list):
    if(len(parameters_list.get(parameter)) < min_length):
        return {
            'parameter': parameter,
            'type': 'format',
            'message': (parameter + ' should be at minimum ' + str(min_length) + ' characters long')
        }