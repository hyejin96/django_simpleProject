# blog 애플리케이션에서 사용할 모든 views를 가져옴
from django.urls import path
from . import views

urlpatterns = [
    # post_list라는 view가 루트 url에 할당됨.
    ## http://localhost:8000/ 주소로 들어왔을때 views.post_list가 보여짐 
    path('', views.post_list, name = 'post_list'),
]