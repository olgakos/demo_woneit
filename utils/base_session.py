from requests import Session

class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        return super().request(method, url=f'{self.base_url}{url}', **kwargs)


def reqres_session():
    return BaseSession(base_url='https://wone-it.ru')
