def check_existence(parameter, parameters_list):
    if(parameter not in parameters_list):
        return {
            'parameter': parameter,
            'type': 'existence',
            'message': (parameter + ' should exist')  
        }

def check_parameter_type(parameter, parameter_type, parameters_list):
    if(type(parameters_list[parameter]) is not parameter_type):
        return {
            'parameter': parameter,
            'type': 'format',
            'message': (parameter + ' should be a ' + str(parameter_type))
        }

def check_in_enum(parameter, parameter_enum, parameters_list):
    if(parameters_list[parameter] not in parameter_enum):
        return {
            'parameter': parameter,
            'type': 'format',
            'message': (parameter + ' should be one of: [' + ','.join(parameter_enum) + ']')
        }