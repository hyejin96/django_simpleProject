from django.shortcuts import render

# Create your views here.

# post_list 함수는 request(요청값)을 넘겨받아 render메서드를 호출하여 받은(return) html을 보여준다.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
