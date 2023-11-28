from django.urls import path, include
from .views import *
products_patterns = [
    path('cart/', cart, name='cart'), #http://127.0.0.1:8000/app/products/cart    path('order/', main, name='order'), #http://127.0.0.1:8000/app/products/order
    path('product/<int:pk>', product, name='product'),]


urlpatterns = [
    path('', main, name='main'),
    path('news/', news, name='news'),
    path('products/<int:id>/', include(products_patterns)),
    path('faq/', faq, name='faq'),
]