from core.context import render_content_by_view_name


def index(view_name, environ):
    context = dict()
    return render_content_by_view_name(view_name, environ, context)
