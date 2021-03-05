from django.contrib import admin
from django.urls import include,path
from . import views
app_name = 'GetItApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.products, name='products'),
    path('search/', views.search_page,  name='search'),
    path('<slug:category_slug>/', views.products, name='products_by_category'),
    path('<int:id>/<slug:slug>', views.product_single, name='single'),
]