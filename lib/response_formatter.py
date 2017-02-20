import dateutil.parser
from datetime import datetime

def _traverse_json_recursive(parameters_list, format_value):
    for key, value in parameters_list.items():
        if type(value) is dict:
            _traverse_json_recursive(value, format_value)
        else:
            parameters_list[key] = format_value(key, value)

def _format_isodatetime(value):
    return dateutil.parser.parse(value)

def _format_month_year_date(value):
    return datetime.strptime(value, '%m%y')

def _format_datetime_based_on_key(key, value):
    if key in ['date_created', 'date_updated', 'boleto_expiration_date']:
        if value is not None:
            return _format_isodatetime(value)
    if key in ['expiration_date']:
        if value is not None:
            return _format_month_year_date(value)
    return value

def _format_datetimes(func):
    def _datetime_formatter(parameters_list):
        response = func(parameters_list)
        _traverse_json_recursive(response, _format_datetime_based_on_key)
        return response
    return _datetime_formatter