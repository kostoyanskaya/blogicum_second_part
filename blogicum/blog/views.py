from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from .models import Category, Post
from blog.constants import POSTS_BY_PAGE


def filter_posts(post_objects):
    return post_objects.filter(
        is_published=True,
        pub_date__lt=now(),
        category__is_published=True
    ).select_related('author', 'location', 'category')


def index(request):
    posts = filter_posts(Post.objects)[:POSTS_BY_PAGE]

    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, id):
    post = get_object_or_404(
        filter_posts(Post.objects),
        id=id,
    )

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = filter_posts(category.posts)

    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': posts}
    )
