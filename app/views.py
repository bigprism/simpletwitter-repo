from django.shortcuts import render

from .models import Post

from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect

from .forms import PostForm

from django.shortcuts import redirect

from .models import Post, Like

from .models import Post, Comment

from .forms import CommentForm


def home(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post).first()
    if not like:
        like = Like(user=request.user, post=post)
        like.save()
    return redirect('post_detail', pk=pk)


def comment_on_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'comment_on_post.html', {'form': form, 'post': post})