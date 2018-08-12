from core.template import skeleton_templates
from settings import templates


def fill_context(text, context):
    for key in context.keys():
        var = '{{ %s }}' % key
        if text.find(var) != -1:
            if not isinstance(context[key], str):
                context[key] = str(context[key])
            text = text.replace(var, context[key])
    return text


def render_template(template, context):
    with open(template, 'r') as template_content:
        content = template_content.read()
        return fill_context(content, context)


def render_content_by_view_name(view_name, environ, context):
    skeleton_templates.update(templates)
    template = skeleton_templates[view_name]
    context.update(environ)
    return render_template(template, context)
