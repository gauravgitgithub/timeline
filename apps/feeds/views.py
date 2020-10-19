from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post

# Create your views here.
@login_required
def feeds(request):
    
    userid = [request.user.id]
    
    for user_posted in request.user.userprofile.follows.all():
        userid.append(user_posted.user.id)

    posts = Post.objects.filter(created_by_id__in=userid)    
    return render(request, 'feed/feeds.html',{'posts':posts})
