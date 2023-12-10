from django.shortcuts import render, redirect

from app_hw.models import Post


def main_page_view(request):
    context = {'post_list': Post.objects.all()}

    return render(request, 'app_hw/index.html', context)


def detail_page_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post_id': post}

    return render(request, 'app_hw/post_detail.html', context)


def create_page_view(request):
    if request.method == 'POST':
        author_post = request.POST.get('author_post')
        title = request.POST.get('title')
        description = request.POST.get('description_post')
        likes = request.POST.get('quantity_likes')
        post = Post()

        post.author_post = author_post
        post.title = title
        post.description_post = description
        post.quantity_likes = likes
        post.save()

        return redirect('main_page')

    return render(request, 'app_hw/post_create.html')

