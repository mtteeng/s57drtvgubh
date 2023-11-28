from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import  HttpResponse
def main(request):
    return HttpResponse ('Главная')
def news(request):
    return HttpResponse ('Новости')
def cart(request, id):
    return HttpResponse (f'Корзина # {id}')
def order(request):
    return HttpResponse ('Мои заказы')
def product(request, id, pk):
    name = request.GET.get('login', 'Неизвестного пользователя')
    return HttpResponse (f'Страница с описанием продуктa # {id}, {pk} для {name}')
def faq(request):
    return HttpResponse ('Ваши вопросы')



