from kink import inject

from src.api.dto.out.Hello import Hello
from src.domain.root.RootService import IRootService


@inject
class RootApi:

    def __init__(self, service: IRootService):
        self.service = service

    def say_hello(self) -> Hello:
        data = self.service.say_hello()
        print(data.name)
        return Hello("dto" + data.name)
