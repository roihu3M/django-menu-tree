from django.shortcuts import render

from .models import Menu

def index(request):
    menu_id = request.GET.get('menu')
    if menu_id == None:
        menu_id = 0
    else:
        menu_id = int(menu_id)
    context = {
        'menus' : Menu.objects.all(),
        'item_id' : request.GET.get('id'),
        'menu_id' : menu_id
    }
    return render(request, 'index.html', context)

