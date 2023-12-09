from kink import di
from sanic import Sanic

from src.infrastructure.views.Root import Root


def init_sanic() -> Sanic:
    app = Sanic("HA")
    return app


def init_app():
    di[Sanic] = init_sanic()
