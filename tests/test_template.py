import mock

from core import template


@mock.patch('os.path.exists')
def test_get_template_path(mocked_exist):
    mocked_exist.return_value = False
    assert template.get_template_path('index') == 'core/templates/index.html'
    assert template.get_template_path('error') == 'core/templates/error.html'
    mocked_exist.return_value = True
    assert template.get_template_path('index') == 'templates/index.html'
    assert template.get_template_path('error') == 'templates/error.html'
