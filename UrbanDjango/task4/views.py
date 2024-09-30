from django.shortcuts import render
from django.views.generic import TemplateView
import templates


# Create your views here.
def main_page(request):
    return render(request, 'fourth_task/main.html')


def book_page(request):
    book_type = ['Книга', 'Статья из журнала', 'Статья из сборника конференции', 'Статья из газеты']
    context = {
        'book_type': book_type
    }
    return render(request, 'fourth_task/books.html', context)


def descript_page(request):
    return render(request, 'fourth_task/descript.html')
