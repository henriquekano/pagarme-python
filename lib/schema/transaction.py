from datetime import datetime
from customer import schema_customer
from split_rule import schema_split_rule

def build_schema_transaction(parameters_dict):
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
        'customer': {
            'schema': schema_customer
        },
        'split_rules': {
            'type': list,
            'all': {
                'schema': schema_split_rule
            }
        }    
    }
    if parameters_dict.get('payment_method', 'credit_card') is 'credit_card':
        if 'card_id' in parameters_dict:
            schema_transaction['card_id'] = {
                'type': str,
                'required': True
            }
        else:
            schema_transaction['card_hash'] = {
                'type': str,
                'required': True
            }
    return schema_transaction