from core import http


def test_response_code_in_string():
    assert http.response_code_in_string((100, 'info')) == '100 info'
