from django.shortcuts import render
from .models import Menu


def my_view(request):
    current_url = request.path
    menu_items = Menu.objects.all()
    for item in menu_items:
        if item.url == current_url:
            item.is_active = True
        else:
            item.is_active = False

    return render(request, 'menu.html', {'menu_items': menu_items})