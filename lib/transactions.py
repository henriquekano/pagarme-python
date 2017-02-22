from schema.transaction import build_schema_transaction
from validators import check_schema, check_api_key
from response_formatter import _format_datetimes, _format_datetimes_on_list
from request_formatter import ensure_api_key, _format_booleans
import pagarme_requests

@ensure_api_key
@check_schema(build_schema_transaction)
@_format_booleans
@_format_datetimes
def transaction_create(parameters):
    response = pagarme_requests.post('/transactions', parameters)
    return response.body

def transaction_capture(id=None, transaction={}, metadata={}, split_rules=[]):
    parameters = {}
    parameters['metadata'] = metadata
    if type(split_rules) is list and len(split_rules) > 0:
        parameters['split_rules'] = split_rules
    @ensure_api_key
    @_format_booleans
    @_format_datetimes
    def _transaction_capture(parameters_dict):
        path = '/transactions/%s/capture' % (str(transaction.get('id', id)))
        response = pagarme_requests.post(path, parameters_dict)
        return response.body
    return _transaction_capture(parameters)

def transaction_refund(id=None, transaction={}, amount=None):
    parameters = {}
    if amount is not None:
        parameters['amount'] = amount
    elif len(transaction) > 0 and amount is None:
        parameters['amount'] = transaction.get('amount', 0)
    @ensure_api_key
    def _transaction_refund(parameters_dict):
        path = '/transactions/%s/refund' % (str(transaction.get('id', id)))
        response = pagarme_requests.post(path, parameters_dict)
        return response.body
    return _transaction_refund(parameters)

@ensure_api_key
@_format_booleans
@_format_datetimes_on_list
def _transaction_find(parameters_dict):
    path = '/transactions'
    response = pagarme_requests.get(path, parameters_dict)
    return response.body

def transaction_find_by_id(id):
    return _transaction_find({'id': id})
