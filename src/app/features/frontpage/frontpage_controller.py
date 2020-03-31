from quart import Blueprint, render_template

frontpage_bp: Blueprint = Blueprint("frontpage", __name__, template_folder="./")

@frontpage_bp.route("/")
async def index():
    return await render_template("index.html")