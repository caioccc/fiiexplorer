# coding=utf-8
"""
This module is a Tool to render template block.
"""
from django.template import loader, Context


def get_template(template):
    """
    This method transform template path to Template Object
    :param template: template path
    :return: Template Object
    """
    if isinstance(template, (tuple, list)):
        return loader.select_template(template)
    return loader.get_template(template)


def render_block_to_string(template_name, dictionary=None, context_instance=None):
    """
    Loads the given template_name and renders the given block with the given dictionary as
    context. Returns a string.
    """
    dictionary = dictionary or {}
    template = get_template(template_name)
    if context_instance:
        context_instance.update(dictionary)
    else:
        context_instance = Context(dictionary)
    return template.render(context_instance)
