from address import schema_address
from phone import schema_phone

schema_customer = {
    'name': {
        'type': str
    },
    'document_number': {
        'type': str,
        'min-length': 11
    },
    'email': {
        'type': str
    },
    'phone': {
        'schema': schema_phone
    },
    'address': {
        'schema': schema_address
    }
}