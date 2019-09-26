# 모델과 템플릿을 연결해주는 역할

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

# post_list 함수는 request(요청값)을 넘겨받아 render메서드를 호출하여 받은(return) html을 보여준다.
def post_list(request):
    # publish_date__lte: 과거에 작성한 글
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts}) # '매개변수' : 쿼리셋
