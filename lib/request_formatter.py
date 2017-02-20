from configurations import _configuration
from response_formatter import _traverse_json_recursive
def ensure_api_key(func):
    def _add_api_key(parameters_dict):
        if 'api_key' not in parameters_dict:
            parameters_dict['api_key'] = _configuration['api_key']
        return func(parameters_dict)
    return _add_api_key

def _filter_none_values(**kwargs):
    return {key: value for key, value in kwargs.iteritems() if value is not None}

def _format_boolean_to_string(key, value):
    if type(value) is bool:
        return str(value).lower()
    return value

def _format_booleans(func):
    def _formatter(parameters_dict):
        _traverse_json_recursive(parameters_dict, _format_boolean_to_string)
        return func(parameters_dict)
    return _formatter