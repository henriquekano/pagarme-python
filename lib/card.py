import dateutil.parser
from Crypto.PublicKey import RSA

def make_card_hash(number, expiration_date, holder_name, cvv, public_key, id):
    querystring = 'card_number=%s&card_holder_name=%s&card_expiration_date=%s&card_cvv=%s'.format(number, holder_name, expiration_date, cvv)
    public_key = RSA.importKey(public_key)
    encrypted = public_key.encrypt('encrypt this message', 32)
    return id + '_' + encrypted