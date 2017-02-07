from transactions import transaction_create

print transaction_create({
  "api_key":"ak_test_zXjKL8u5uxn25HNxHviPbhthNV0nL7",
  "plan":{
    "amount":31000,
    "days":30,
    "name":"Plano Ouro",
    "payments_methods": [
      "boleto", "credit_card"
    ]
  },
  "card_number": "4242424242424242",
  "card_cvv": "122",
  "card_holder_name": "SDFSDF",
  "card_expiration_date": "1220",
  "customer":{
    "email":"email.do.cliente@gmail.com",
    "name":"nome",
    "document_number":"{{CPF}}",
    "address":{
      "zipcode":"{{CEP}}",
      "neighborhood":"bairro",
      "street":"rua",
      "street_number":"122"
    },
    "phone": {
      "number":"87654321",
      "ddd":"11"
    }
  } ,
  "capture": False,
  "payment_method":"credit_card",
  "amount": 122,
  "split_rules": [
    {
      "recipient_id": "re_civb4p9l7004xbm6dhsetkpj8",
      "percentage": 50,
      "liable": True,
      "charge_processing_fee": True
    },{
      "recipient_id": "re_civb4o6zr003u3m6e8dezzja6",
      "percentage": 50,
      "liable": True,
      "charge_processing_fee": True
    }
  ]
})