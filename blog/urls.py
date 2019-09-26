# blog 애플리케이션에서 사용할 모든 views를 가져옴
from django.urls import path
from . import views

urlpatterns = [
    # post_list라는 view가 루트 url에 할당됨.
    ## http://localhost:8000/ 주소로 들어왔을때 views.post_list가 보여짐 
    path('', views.post_list, name = 'post_list')
    # /은 다음에 / 가 한 번 더 와야 한다는 의미입니다.
    , path('post/<int:pk>/', views.post_detail, name = 'post_detail')
    , path('post/new/', views.post_new, name = 'post_new')
    , path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]