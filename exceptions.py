class DataSourceBrokenException(Exception):
    """Класс для ошибки, когда файл поврежден"""
    pass

class PictureFormatNotSupportedError(Exception):
    """Класс для ошибки, когда формат файла не поддерживается"""
    pass

class PictureNotUploadedError(Exception):
    """Класс для ошибки загрузки файла"""
    pass