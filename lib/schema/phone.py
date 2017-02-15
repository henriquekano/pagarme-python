schema_phone = {
	'ddd': {
		'required': True,
		'type': str,
		'max-length': 2,
		'min-length': 2
	},
	'number': {
		'required': True,
		'type': str,
		'max-length': 9,
		'min-length': 8
	},
	'ddi': {
		'max-length': 2,
		'min-length': 2
	}
}