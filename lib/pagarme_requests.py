import requests
from configurations import get_full_url
from pagarme_response import PagarmeResponse

def _do_request(verb, url, parameters):
    if verb in ['POST', 'PUT']:
        r = requests.request(verb, url, json=parameters)
    elif verb in ['GET']:
        r = requests.request(verb, url, params=parameters)
    return PagarmeResponse(r)

def post(path, parameters):
    return _do_request('POST', get_full_url(path), parameters)

def get(path, parameters):
    return _do_request('GET', get_full_url(path), parameters)