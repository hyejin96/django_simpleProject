from django import forms
from .models import Post

# 폼이 ModelForm이라는 것을 알려줘야 한다.
class PostForm(forms.ModelForm):
    # class Meta : 이 폼을 만들기 위해서 어떤 모델이 쓰여야 하는지 장고에 알려주는 구문
    class Meta:
        model = Post
        fields = ('title', 'text',)