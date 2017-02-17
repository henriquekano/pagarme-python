from schema.transaction import build_schema_transaction
from validators import check_schema, check_api_key
from response_formatter import format_datetimes
from request_formatter import ensure_api_key, format_to_dict, format_booleans
from configurations import get_full_url
import requests

@ensure_api_key
@check_api_key
@check_schema(build_schema_transaction)
@format_booleans
@format_datetimes
def transaction_create(parameters):
    url = get_full_url('/transactions')
    r = requests.post(url, data = parameters)
    return r.json()

@format_to_dict
@ensure_api_key
@check_api_key
@format_booleans
@format_datetimes
def transaction_capture(transaction={}, id=None, metadata=None, split_rules=None):
    url = get_full_url('/transactions/%s/capture'.format(transaction.get('id', id)))
    print parameters, 'asdasdasd'
    r = requests.post(url, data = parameters)
    return r.json()