schema_split_rule = {
	'recipient_id': {
		'type': str,
		'required': True
	},
	'charge_processing_fee': {
		'type': bool
	},
	'liable': {
		'type': bool
	},
	'charge_remainder': {
		'type': bool
	},
	'or': [
		{
			'percentage': {
				'type': int,
				'max': 100,
				'min': 0,
				'required': True
			},
			'amount': {
				'type': int,
				'min': 0,
				'required': True
			}
		}
	]
}