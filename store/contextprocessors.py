from store.models import Category

def menus(request):
    menu_item = Category.objects.filter(parent = None)
    return dict(menu_item=menu_item)