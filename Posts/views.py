from django.shortcuts import render, redirect, get_object_or_404
from .models import PostModel 
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import  CommentModel
from .forms import CommentForm



@login_required
def homepage_view(request):
    posts = PostModel.objects.all().order_by('-created_at')
    return render(request, 'homepage.html', {'posts': posts})

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('homepage')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Unlike
    else:
        post.likes.add(request.user)  # Like
    return redirect('homepage')


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)
    comments = post.comments.all().order_by('-created_at')
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'post_detail.html', context)
