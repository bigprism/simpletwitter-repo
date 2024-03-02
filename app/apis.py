from django.http import JsonResponse

from .models import Post

from .models import Post, Like

from .models import Post, Comment


def get_posts(request):
    posts = Post.objects.all().order_by('-timestamp')
    data = [post.to_dict() for post in posts]
    return JsonResponse({'posts': data})


def create_post(request):
    if request.method == 'POST':
        data = request.POST.dict()
        post = Post.objects.create(**data)
        return JsonResponse({'post': post.to_dict()})


def like_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            like = Like(user=request.user, post=post)
            like.save()
        return JsonResponse({'success': True})


def comment_on_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        data = request.POST.dict()
        comment = Comment.objects.create(**data)
        return JsonResponse({'comment': comment.to_dict()})