from decorators import check_api_key
import requests

@check_api_key
def transaction_create(parameters):
    print parameters
    r = requests.post('https://api.pagar.me/1/transactions', data = parameters)
    return r.json()