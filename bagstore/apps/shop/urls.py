from django.urls import re_path

from apps.shop import views

urlpatterns = [
    re_path(r'^$', views.ShopPageView.as_view(), name='shop'),
]
