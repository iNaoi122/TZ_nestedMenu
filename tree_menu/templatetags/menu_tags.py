from django import template
from django.template import Template, Context
from tree_menu.models import *

register = template.Library()


@register.simple_tag()
def draw_all_branch():
    menu_items = Branch.objects.filter(parent=None)

    def render_branch(menu_items):
        print(menu_items)
        if not menu_items:
            return ''

        output = '<ul>'

        for item in menu_items:
            context = Context({'url': f'{item.url}', 'title': f'{item.title}'})
            if not item.children:
                output += '<li><a href = "{{ url }}">{{ title }}</a></li>'
            else:
                output += '<li><a href = "{{ url }}">{{ title }}</a></li>'
                output += render_branch(item.children.all())
                output += '</li>'

            output += '</ul>'
            output = Template(output).render(context)

        return output

    return render_branch(menu_items)


@register.simple_tag()
def test():
    items = Branch.objects.all()
    return items
