import os
import random
import utils
from flask import Blueprint, render_template, request, current_app

from exceptions import PictureFormatNotSupportedError, PictureNotUploadedError

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/post', methods=['GET'])
def page_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def page_create_post():
    picture = request.files.get('picture', None)
    content = request.values.get('content', '')

    # Работаем с картинкой

    filename = picture.filename
    file_type = filename.split('.')[-1]

    #Проверяем валидность картинки

    if not is_file_type_valid(file_type):
        raise PictureFormatNotSupportedError(f"Формат {file_type} не поддерживается")

    # Генерируем название для картинки
    pic_name = str(random.randint(0, 10))
    filename_to_save = f"{pic_name}.{file_type}"
    os_path = os.path.join(".", "uploads", filename_to_save)
    is_filename_occupied = os.path.exists(os_path)

    #Проверка загрузки файла
    try:
        picture.save(os_path.join(filename_to_save))
    except FileNotFoundError:
        raise PictureNotUploadedError(f"{filename_to_save}")

    web_path = f"/uploads/{filename_to_save}"
    pic = web_path

    return render_template('post_uploaded.html', pic=pic, content=content)

def is_file_type_valid(file_type):
    if file_type.lower() in ["jpg", "jpeg", "png", "gif", "webp", "tiff"]:
        return True
    return False

@loader_blueprint.errorhandler(PictureFormatNotSupportedError)
def error_format_not_supported(e):
    return "Формат картинки не поддерживается выберите другой"

@loader_blueprint.errorhandler(PictureNotUploadedError)
def uploaded_error(e):
    return "Ошибка загрузки файла"