from django.core.management.base import BaseCommand, CommandError
from menu.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        menu = Menu.objects.create(title='1')
        for i in range(1, 4):
            title1 = '1.' + str(i)
            Item.objects.create(title=title1, menu=menu, parent=None)
            for j in range(1, 4):
                title2 = title1 + '.' + str(j)
                Item.objects.create(title=title2, menu=menu, parent=Item.objects.get(title=title1))
                for k in range(1, 4):    
                    title3 = title2 + '.' + str(k)
                    Item.objects.create(title=title3, menu=menu, parent=Item.objects.get(title=title2))
                    for l in range(1, 4):
                        title4 = title3 + '.' + str(l)
                        Item.objects.create(title=title4, menu=menu, parent=Item.objects.get(title=title3))
        menu2 = Menu.objects.create(title='2')
        for i in range(1, 5):
            title1 = '2.' + str(i)
            Item.objects.create(title=title1, menu=menu2, parent=None)
            for j in range(1, 5):
                title2 = title1 + '.' + str(j)
                Item.objects.create(title=title2, menu=menu2, parent=Item.objects.get(title=title1))
                for k in range(1, 5):    
                    title3 = title2 + '.' + str(k)
                    Item.objects.create(title=title3, menu=menu2, parent=Item.objects.get(title=title2))
                    for l in range(1, 5):
                        title4 = title3 + '.' + str(l)
                        Item.objects.create(title=title4, menu=menu2, parent=Item.objects.get(title=title3))