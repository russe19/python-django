from django.core.exceptions import PermissionDenied
from loguru import logger
import time


class LogData:
    logger.add("debug.log", format="{time} | {message}", level="INFO",
               rotation="100 MB", compression="zip")

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        logger.info(f"Запрошенный путь: {request.META['HTTP_HOST']}{request.META['PATH_INFO']} | {request.META['REQUEST_METHOD']}")

        response = self.get_response(request)

        return response