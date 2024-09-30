from django.shortcuts import render
from django.views.generic import TemplateView
import templates


# Create your views here.
def main_page(request):
    return render(request, 'third_task/main.html')


def book_page(request):
    return render(request, 'third_task/books.html')


class descripton(TemplateView):
    template_name = 'third_task/descript.html'
