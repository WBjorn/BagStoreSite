from django.views.generic import TemplateView

class MainPageView(TemplateView):
    '''Отображение главной страницы'''
    template_name = 'index.html'

class ShopPageView(TemplateView):
    '''Отображение магазина'''
    template_name = 'shop.html'
    