from os.path import abspath
from logging import Logger, FileHandler, StreamHandler, DEBUG
from app_logger import *
from pytest import raises


def test_get_file_handler():
    handler = get_file_handler()

    # Проверяем что возвращается объект именно типа FileHandler
    assert isinstance(handler, FileHandler)
    assert handler.level == DEBUG
    assert handler.baseFilename == abspath('new.log')


def test_get_stream_handler():
    handler = get_stream_handler()

    assert isinstance(handler, StreamHandler)
    assert handler.level == DEBUG


def test_get_logger():
    logger = get_logger('Feature')
    assert isinstance(logger, Logger)
    assert logger.name == 'Feature'
    assert len(logger.handlers) == 2


# Тест проверяет что в случае если вызвать get_logger без аргументов, получим TypeError
def test_get_logger_call_without_name():
    with raises(TypeError):
        get_logger()

