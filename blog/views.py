from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    all_post = Post.objects.all().order_by('id')
    paginator = Paginator(all_post, 4, orphans=2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'page_obj': page_obj})
    