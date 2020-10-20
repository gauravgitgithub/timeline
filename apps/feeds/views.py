from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Post
from .models import Like

# Create your views here.


@login_required
def feeds(request):

    userid = [request.user.id]

    for user_posted in request.user.userprofile.follows.all():
        userid.append(user_posted.user.id)

    posts = Post.objects.filter(created_by_id__in=userid)
    for post in posts:
        likes = post.likes.filter(created_by_id=request.user.id)
        if likes.count() > 0:
            post.liked = True
        else:
            post.liked = False

    return render(request, 'feed/feeds.html', {'posts': posts})


@login_required
def search(request):
    query = request.GET.get('query', '')
    if len(query) > 0:
        users = User.objects.filter(username__icontains=query)
    else:
        users = []

    context = {
        'query': query,
        'matches': users
    }

    return render(request, 'feed/search.html', context)
