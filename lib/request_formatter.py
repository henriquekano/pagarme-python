from configurations import _configuration

def ensure_api_key(func):
    def _add_api_key(parameters_dict):
        if 'api_key' not in parameters_dict:
            parameters_dict['api_key'] = _configuration['api_key']
        return func(parameters_dict)
    return _add_api_key
