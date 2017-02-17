_configuration = {
    'endpoint': 'https://api.pagar.me',
    'version': '1',
    'api_key': '',
    'encryption_key': ''
}

def PagarMeInit(new_api_key, new_encryption_key = ''):
    _configuration['api_key'] = new_api_key
    _configuration['encryption_key'] = new_encryption_key

def get_full_url(path):
    return _configuration['endpoint'] + '/' + _configuration['version'] + path