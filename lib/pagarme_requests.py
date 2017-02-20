import requests
from configurations import get_full_url
from pagarme_response import PagarmeResponse

def _do_request(verb, url, parameters):
    r = requests.request(verb, url, json=parameters)
    return PagarmeResponse(r)

def post(path, parameters):
    return _do_request('POST', get_full_url(path), parameters)