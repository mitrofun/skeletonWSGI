import mock
from importlib import reload

import settings
from core import context


def test_fill_context():
    assert context.fill_context('', {}) == ''
    text = '<div>{{ name }}</div>'
    items = {'name': 'Ivan'}
    assert context.fill_context(text, items) == '<div>Ivan</div>'


def test_render_template(template):
    items = {'title': 'Page'}
    assert context.render_template(template, items) == '<div>Page</div>'


@mock.patch.dict(settings.templates, {'index': 'fixtures/template.html'})
def test_render_content_by_view_name():
    reload(context)
    items = {'title': 'New'}
    assert context.render_content_by_view_name('index', dict(), items) == '<div>New</div>'
