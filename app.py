from flask import Flask, send_from_directory
import utils
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging
import loggers


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config["POST_PATH"] = "posts.json"
app.config["UPLOAD_FOLDER"] = "uploads/images"

loggers.create_loggers()

logger = logging.getLogger("basic")


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

logger.info("Приложение запускается")
app.run()
