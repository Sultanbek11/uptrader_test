from django import template
from django.core.cache import cache
from treemenu.models import Menu


register = template.Library()


@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = Menu.objects.filter(title=menu_name)

    if menu_items is None:
        menu_items = Menu.objects.filter(...)
        cache.set('menu_items', menu_items, 300)

    def build_menu_structure(items, depth=0, max_depth=10):
        if depth >= max_depth:
            return []
        menu_structure = []
        for item in items:
            submenu = build_menu_structure(Menu.objects.filter(parent=item), depth=depth + 1, max_depth=max_depth)
            menu_structure.append({
                'title': item.title,
                'url': item.url,
                'is_active': current_url == item.url,
                'submenu': submenu,
            })
        return menu_structure

    menu_structure = build_menu_structure(menu_items)

    def render_menu(menu):
        menu_html = '<ul>'
        for item in menu:
            menu_html += f'<li><a href="{item["url"]}"'
            if item['is_active']:
                menu_html += ' class="active"'
            menu_html += f'>{item["title"]}</a>'
            if item['submenu']:
                menu_html += render_menu(item['submenu'])
            menu_html += '</li>'
        menu_html += '</ul>'
        return menu_html

    menu_html = render_menu(menu_structure)

    return menu_html