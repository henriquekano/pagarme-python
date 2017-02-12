import dateutil.parser

def format_datetimes(func):
    def parameters_wrapper(parameters_list):
        return_value = func(parameters_list)
        return_value['date_created'] = dateutil.parser.parse(return_value['date_created'])
        return_value['date_updated'] = dateutil.parser.parse(return_value['date_updated'])
        return return_value
    return parameters_wrapper