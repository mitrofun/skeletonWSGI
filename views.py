# this example how use skeleton
# uncomment this code for use custom view
"""
from core.context import render_content_by_view_name


def index(view_name, environ):
    context = {
        'title': 'Страница вашего проекта',
        'page_header': 'Заголовок страницы вашего проекта',
        'text': 'Рандомный текст для страницы проекта.',
        'footer': 'Подвал проекта'
    }

    return render_content_by_view_name(view_name, environ, context)

def contacts(view_name, environ):
    context = {
        'title': 'Page contact',
        'page_header': 'Our contacts',
        'email': 'email@domain.com'
    }

    return render_content_by_view_name(view_name, environ, context)
"""
