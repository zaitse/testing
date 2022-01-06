import os
import logging
from app_logger import *


def test_log_file_created(clean_log_file):
    assert not os.path.exists('new.log')
    logger = get_logger('logger1')
    logging.shutdown()
    assert os.path.exists('new.log')


def test_log_records_created(clean_log_file):
    assert not os.path.exists('new.log')
    logger = get_logger('logger2')
    logger.info('info message')
    logger.warning('warning message')
    logger.debug('debug message')
    logging.shutdown()
    assert os.path.exists('new.log')

    with open('new.log') as f:
        lines = f.readlines()
        for level in ['DEBUG', 'INFO', 'WARNING']:
            assert any([True for line in lines if level in line])
