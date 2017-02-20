class PagarmeResponse():
    def __init__(self, response):
        self._response = response

    @property
    def body(self):
        return self._response.json()

    @property
    def headers(self):
        return self._response.headers

    @property
    def status_code(self):
        return self._response.status_code