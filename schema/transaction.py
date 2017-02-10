from datetime import datetime
from customer import schema_customer
schema_transaction = {
    'payment_method': {
        'type': str,
        'required': True,
        'enum': [
            'credit_card', 'boleto'
        ],
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
        'schema': schema_customer
    },
    'split_rules': {
        'all': {
            'schema': ''
        }
    }
    
}