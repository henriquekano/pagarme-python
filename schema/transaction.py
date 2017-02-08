schema_transaction = {
    'payment_method': {
        'type': str,
        'required': True,
        'enum': ['credit_card', 'boleto']
    },
    'amount': {
        'type': int,
        'required': True
    }
}