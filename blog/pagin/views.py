from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size', 4)
    paginator = Paginator(posts, page_size)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    context = {
        'page_posts': page_posts,
        'page_size': page_size
    }
    return render(request, 'post_list.html', context)
