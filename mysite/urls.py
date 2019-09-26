"""
여러줄 주석
"""
# include 함수 : blog.urls를 가져오기 위해 사용
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls)
    , path('', include('blog.urls'))
]
