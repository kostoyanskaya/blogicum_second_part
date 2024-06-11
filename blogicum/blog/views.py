from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils.timezone import now


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lt=now(),
        category__is_published=True,)[:5]

    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lt=now(),
            category__is_published=True,
        ),
        id=id,
    )

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = Post.objects.filter(
        category=category,
        pub_date__lt=now(),
        is_published=True
    )
    context = {'post_list': posts}
    return render(
        request,
        'blog/category.html',
        context
    )
