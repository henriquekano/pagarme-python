import dateutil.parser

def format_datetimes(func):
    def _datetime_formatter(parameters_list):
        return_value = func(parameters_list)
        date_created = return_value.get('date_created')
        date_updated = return_value.get('date_updated')
        if date_created is not None:
        	return_value['date_created'] = dateutil.parser.parse(date_created)
        if date_updated is not None:
        	return_value['date_updated'] = dateutil.parser.parse(date_updated)
        return return_value
    return _datetime_formatter