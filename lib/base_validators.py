def _format_error(parameter_name, type_name, message):
    return {
        'parameter': parameter_name,
        'type': type_name,
        'message': message
    }


def check_existence(parameter, should_exist, parameters_list):
    if(parameter not in parameters_list and should_exist):
        return _format_error(
            parameter,
            'existence',
            (parameter + ' should exist')
        )


def check_parameter_type(parameter, parameter_type, parameters_list):
    if(type(parameters_list.get(parameter)) is not parameter_type):
        return _format_error(
            parameter,
            'format',
            (str(parameter) + ' should be a ' + str(parameter_type))
        )


def check_in_enum(parameter, parameter_enum, parameters_list):
    if(parameters_list.get(parameter) not in parameter_enum):
        joined_enums = ','.join(
            map(str, parameter_enum)
        )
        return _format_error(
            parameter,
            'format',
            (str(parameter) + ' should be one of: [' + joined_enums + ']')
        )


def check_max(parameter, max_value, parameters_list):
    parameter_value = parameters_list.get(parameter)
    error = _format_error(
        parameter,
        'format',
        (str(parameter) + ' should be at most ' + str(max_value))
    )
    try:
        max_value = int(max_value)
        parameter_value = int(parameter_value)
        if(parameter_value > max_value):
            return error
    except (ValueError, TypeError):
        return error


def check_min(parameter, min_value, parameters_list):
    parameter_value = parameters_list.get(parameter)
    error = _format_error(
        parameter,
        'format',
        (str(parameter) + ' should be, at least, ' + str(min_value))
    )
    try:
        min_value = int(min_value)
        parameter_value = int(parameter_value)
        if(parameter_value < min_value):
            return error
    except (ValueError, TypeError):
        return error


def check_max_length(parameter, max_length, parameters_list):
    parameter_value = parameters_list.get(parameter)
    error = _format_error(
        parameter,
        'format',
        (
            '%s should be, at most, %s characters long'
            .format(str(parameter), str(max_length))
        )
    )
    try:
        max_length = int(max_length)
        parameter_value = str(parameter_value)
        if(len(parameters_list.get(parameter)) > max_length):
            return error
    except (ValueError, TypeError):
        return error


def check_min_length(parameter, min_length, parameters_list):
    parameter_value = parameters_list.get(parameter)
    error = _format_error(
        parameter,
        'format',
        (
            '%s should be, at least, %s characters long'
            .format(str(parameter), str(min_length))
        )
    )
    try:
        min_length = int(min_length)
        parameter_value = str(parameter_value)
        if(len(parameters_list.get(parameter)) < min_length):
            return error
    except (ValueError, TypeError):
        return error
