import os
import pytest


@pytest.fixture
def clean_log_file():
    if os.path.exists('new.log'):
        os.remove('new.log')
    yield
