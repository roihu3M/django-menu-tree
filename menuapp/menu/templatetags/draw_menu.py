from django import template

from menu.models import Item


register = template.Library()

@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, current_menu_id):
    request = context['request']
    items = Item.objects.filter(menu__id=current_menu_id)
    items_values = items.values()
    top_child_items = [item for item in items_values.filter(parent=None)]
    if request.GET.get('id') != '0':
        current_item = items.get(id=request.GET.get('id'))
        parent_chain = get_parent_chain(current_item)
        for parent in top_child_items:
            if parent['id'] in parent_chain:
                parent['children'] = get_child_items(items_values, parent['id'], parent_chain)
        context = {
            'items' : top_child_items, 
            'menu' : current_menu_id
        }
    else: 
        context = {
            'items' : top_child_items, 
            'menu' : current_menu_id
        }
    return context

def get_parent_chain(item):
    parent_chain_ids = []
    while item != None:
        parent_chain_ids.insert(0, item.id)
        item = item.parent
    return parent_chain_ids

def get_child_items(item_values, current_parent_id, expanded_items_id_list):
    current_parent_child_list = [
        item for item in item_values.filter(parent_id=current_parent_id)
    ]
    for child in current_parent_child_list:
        if child['id'] in expanded_items_id_list:
            child['children'] = get_child_items(
                item_values, child['id'], expanded_items_id_list
            )
    return current_parent_child_list
