from lib.card import make_card_hash

class Card(unittest.TestCase):
	def test_card_hash_maker(self):
		card_hash = make_card_hash('4901720080344448', '1213', 'Usuario de Teste', '314', '-----BEGIN PUBLIC KEY-----\ -----END PUBLIC KEY-----\ ', '1')