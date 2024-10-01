from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_django(request):
    users = ['Vanya', 'Petya', 'Kolya', 'Sacha']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            if username not in users and password == repeat_password and age >= 18:
                return HttpResponse(f'Приветствуем, {username}')
            else:
                if username in users:
                    info['error1'] = 'Пользователь уже существует'
                if password != repeat_password:
                    info['error2'] = 'Пароли не совпадают'
                if age < 18:
                    info['error3'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', context=info)
    else:
        form = UserRegister()
        info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_html(request):
    users = ['Vasya', 'P`er', 'Kolins', 'Sancho']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if username not in users and password == repeat_password and age >= 18:
            return HttpResponse(f'Приветствуем, {username}')
        else:
            if username in users:
                info['error1'] = 'Пользователь уже существует'
            if password != repeat_password:
                info['error2'] = 'Пароли не совпадают'
            if age < 18:
                info['error3'] = 'Вы должны быть старше 18'
            return render(request, 'fifth_task/registration_page.html', context=info)

    return render(request, 'fifth_task/registration_page.html', context=info)
