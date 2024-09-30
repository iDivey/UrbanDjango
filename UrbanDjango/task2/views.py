from django.shortcuts import render
from django.views.generic import TemplateView
import templates


# Create your views here.
def func(request):
    return render(request, 'second_task/func.html')


class cls(TemplateView):
    template_name = 'second_task/cls.html'
