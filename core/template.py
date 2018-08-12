import os

skeleton_templates = {
    'index': 'core/templates/index.html',
    'error': 'core/templates/error.html'
}


def get_template_path(template_name):
    custom_path = 'templates/%s.html' % template_name
    if os.path.exists(custom_path):
        return custom_path
    else:
        return 'core/templates/%s.html' % template_name
