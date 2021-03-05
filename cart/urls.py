from django.contrib import admin
from django.urls import include,path, re_path
from . import views
app_name = 'cart'
urlpatterns = [
    path('', views.cart_table, name='cart_table'),
    #path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    re_path('add/(?P<product_id>[0-9]+)/$', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),
]