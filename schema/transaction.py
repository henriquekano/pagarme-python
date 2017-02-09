from datetime import datetime
schema_transaction = {
    'payment_method': {
        'type': str,
        'required': True,
        'enum': [
            'credit_card', 'boleto'
        ],
        'credit_card': {
            'or': [
                    {
                    'card_number': {
                        'type': str,
                        'required': True,
                        'length': 16,
                        'enum': ['credit_card', 'boleto']
                    },
                    'card_cvv': {
                        'type': str,
                        'required': True,
                        'min_length': 3,
                        'max_length': 4
                    },
                    'card_holder_name': {
                        'type': str,
                        'required': True
                    },
                    'card_expiration_date': {
                        'type': datetime,
                        'format': 'MMyy',
                        'required': True
                    }
                },{
                    'card_id': {
                        'type': str,
                        'required': True
                    }
                },{
                    'card_hash': {
                        'type': str,
                        'required': True
                    }
                }
            ]
        }
    },
    'amount': {
        'type': int,
        'required': True
    },
    'postback_url': {
        'type': str
    },
    'async': {
        'type': bool
    },
    'installments': {
        'type': int,
        'max': 12,
        'min': 1
    },
    'boleto_expiration_date': {
        'type': datetime,
        'format': 'timestamp'
    },
    'boleto_instructions': {
        'type': str,
        'max_length': 255
    },
    'soft_descriptor': {
        'type': str,
        'max_length': 13
    },
    'capture': {
        'type': bool
    },
    'metadata': {
        'type': dict
    },
    'customer': {
        'schema': ''
    },
    'split_rules': {
        'all': {
            'schema': ''
        }
    }
    
}