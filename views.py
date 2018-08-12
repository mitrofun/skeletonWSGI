from core.context import render_content_by_view_name


# this example how use skeleton
def index(view_name, environ):
    context = {
        'title': 'Страница вашего проекта',
        'page_header': 'Заголовок страницы вашего проекта',
        'text': 'Рандомный текст для страницы проекта.',
        'footer': 'Подвал проекта'
    }

    return render_content_by_view_name(view_name, environ, context)
