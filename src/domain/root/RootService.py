from kink import inject
from src.domain.root.RootData import RootData


class IRootService:

    def say_hello(self) -> RootData:
        pass


@inject(alias=IRootService)
class RootService(IRootService):

    def __init__(self):
        pass

    def say_hello(self) -> RootData:
        print("hello service")
        return RootData("name")
