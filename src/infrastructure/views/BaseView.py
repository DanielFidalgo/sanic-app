from sanic import Sanic


class BaseView:

    @staticmethod
    def configure(app: Sanic, view, path: str):
        app.add_route(view, path)
