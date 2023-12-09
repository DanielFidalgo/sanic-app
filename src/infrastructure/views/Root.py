import dataclasses

from kink import inject
from sanic import json, Sanic
from sanic.views import HTTPMethodView

from src.api.RootApi import RootApi
from src.infrastructure.views.BaseView import BaseView


@inject
class Root(HTTPMethodView, BaseView):

    def __init__(self, api: RootApi):
        self.api = api

    async def get(self, request):
        dto = self.api.say_hello()
        dict_dto = dataclasses.asdict(dto)
        return json(dict_dto)
