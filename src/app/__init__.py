from quart import Quart
from app.features.frontpage.frontpage_controller import frontpage_bp


def create_app() -> Quart:

    app: Quart = Quart(__name__)

    app.register_blueprint(frontpage_bp)

    return app