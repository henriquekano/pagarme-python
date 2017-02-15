schema_address = {
	'zipcode': {
		'type': str,
		'min-length': 8
	},
	'neighborhood': {
		'required': True,
		'type': str
	},
	'street': {
		'required': True,
		'type': str
	},
	'street_number': {
		'required': True,
		'type': str
	},
	'city': {
		'type': str
	},
	'state': {
		'type': str
	}
}