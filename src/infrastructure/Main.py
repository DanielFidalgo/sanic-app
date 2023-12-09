from kink import di
from sanic import Sanic
from src.infrastructure.cdi.AppModule import init_app
from src.infrastructure.views.Root import Root


def main() -> Sanic:
    init_app()
    app = di[Sanic]
    configure_views(app)
    return app


def configure_views(app: Sanic):
    Root.configure(app, Root.as_view(), "/")


if __name__ == "__main__":
    main().run()
    
