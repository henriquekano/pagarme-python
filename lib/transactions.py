from schema.transaction import build_schema_transaction
from validators import check_schema, check_api_key
from response_formatter import format_datetimes
from request_formatter import ensure_api_key
from configurations import get_full_url
import requests

@ensure_api_key
@check_api_key
@check_schema(build_schema_transaction)
@format_datetimes
def transaction_create(parameters):
    url = get_full_url('/transactions')
    r = requests.post(url, data = parameters)
    return r.json()