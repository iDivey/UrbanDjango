from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from task1.forms import UserRegister
from task1.models import *


# Create your views here.
def main_page(request):
    return render(request, 'one_task/main.html')


def game_page(request):
    game_type = Game.objects.all()
    context = {
        'game_type': game_type
    }
    return render(request, 'one_task/games.html', context)


def descript_page(request):
    game_type = Game.objects.all()
    context = {
        'game_type': game_type
    }
    return render(request, 'one_task/descript.html', context)


def sign_up_by_django(request):
    users = []
    user_all = Buyer.objects.values_list("name", flat=True)
    for user in user_all:
        users.append(user)
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            if username not in users and password == repeat_password and age >= 18:
                Buyer.objects.create(name=username, age=age, balance=0.0)
                return HttpResponse(f'Приветствуем, {username}')
            else:
                if username in users:
                    info['error1'] = 'Пользователь уже существует'
                if password != repeat_password:
                    info['error2'] = 'Пароли не совпадают'
                if age < 18:
                    info['error3'] = 'Вы должны быть старше 18'
                return render(request, 'one_task/registration_page.html', context=info)
    else:
        form = UserRegister()
        info['form'] = form
    return render(request, 'one_task/registration_page.html', context=info)
