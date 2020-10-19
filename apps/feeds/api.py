import json

from django.http import JsonResponse
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def add_new_post(request):
    data = json.loads(request.body)
    body = data['body']
    
    post = Post.objects.create(body=body, created_by=request.user)
    
    
    return JsonResponse({'success':True})
    