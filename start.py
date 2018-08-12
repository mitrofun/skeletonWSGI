import views
from core import views as skeleton_views
from core import status
from core.context import render_template
from core.http import response_code_in_string
from core.template import get_template_path
from settings import route


def get_view(url, urls):
    return urls.get(url, None)


def application(environ, start_response):
    url = environ['REQUEST_URI']

    headers = [('Content-Type', 'text/html; charset: utf-8')]
    view_name = get_view(url, route)

    if not view_name:
        response_status = status.HTTP_404_NOT_FOUND
        context = {
            'code_error': status.HTTP_404_NOT_FOUND[0],
            'text_error': status.HTTP_404_NOT_FOUND[1]
        }
        context.update(environ)
        template = get_template_path('error')
        content = render_template(template, context)
    else:
        response_status = status.HTTP_200_OK
        try:
            content = getattr(views, view_name)(view_name, environ)
        except AttributeError:
            content = getattr(skeleton_views, view_name)(view_name, environ)

    start_response(response_code_in_string(response_status), headers)
    return bytes(content, 'utf-8')
