from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('checkout/', views.order_create, name='order_create'),
    path('service/checkout/', views.order, name='order'),
    path('special/checkout/', views.order_for_special, name='special'),
]