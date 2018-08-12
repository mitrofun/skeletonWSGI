import os
import sys

import pytest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, os.path.join(ROOT_DIR, 'core'))


@pytest.fixture
def root_path():
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


@pytest.fixture
def template(root_path):
    return os.path.join(root_path, 'fixtures', 'template.html')
