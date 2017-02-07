def check_existence(parameter, parameters_list):
	if(parameter not in parameters_list):
		raise ValueError(parameter + 'should be present')

def check_parameter_type(parameter, parameter_type, parameters_list):
	if(type(parameters_list[parameter]) is not parameter_type):
		raise ValueError(parameter + 'should be a' + parameter_type)


def check_api_key(func):
	def wrapper(parameters_list):
		check_existence('api_key', parameters_list)
		check_parameter_type('api_key', str, parameters_list)
		func(parameters_list)
	return wrapper