from schema.transaction import schema_transaction
from validators import check_schema, check_api_key
from response_formatter import format_datetimes
from configurations import api_key, endpoint, version
import requests

@check_api_key
@check_schema(schema_transaction)
@format_datetimes
def transaction_create(parameters):
    r = requests.post(endpoint + '/' + version + '/' + 'transactions', data = parameters)
    return r.json()