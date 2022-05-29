import logging
import loggers

from flask import Blueprint, render_template, request
import utils
from exceptions import DataSourceBrokenException

main_blueprint = Blueprint('main_blueprint', __name__)

logger = logging.getLogger("basic")

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

@main_blueprint.route('/search/')
def search_page():
    s = request.values.get("s", None)

    logger.info(f"Выполняется поиск {s}")

    posts = utils.search_post(s)
    data = utils.get_all()
    if s is None or s == "":
        posts = utils.get_all()
    else:
        posts = utils.search_post(s)

    return render_template('post_list.html', s=s, posts=posts)

@main_blueprint.errorhandler(DataSourceBrokenException)
def data_source_broken_error(e):
    return "Файл с данными поврежден, обратитесь к администратору"