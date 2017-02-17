from configurations import _configuration
from response_formatter import _traverse_json_recursive
def ensure_api_key(func):
    def _add_api_key(parameters_dict):
        if 'api_key' not in parameters_dict:
            parameters_dict['api_key'] = _configuration['api_key']
        return func(parameters_dict)
    return _add_api_key

def format_to_dict(func):
    def _group_parameters(**kwargs):
        parameters = {}
        for key, value in kwargs:
            if type(value) is dict:
                parameters.update(value)
            elif value is not None:
                parameters[key] = value
        return parameters
    return _group_parameters

def _format_boolean_to_string(key, value):
    return str(value)

def format_booleans(func):
    def _formatter(parameters_dict):
        _traverse_json_recursive(parameters_dict, _format_boolean_to_string)
        return func(parameters_dict)
    return _formatter