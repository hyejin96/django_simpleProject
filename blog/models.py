# from 또는 import로 시작하는 부분: 다른 파일에 있는 것을 추가하라.
from django.conf import settings
from django.db import models
from django.utils import timezone

# 모델(객체) 정의
## class : 객체를 정의한다.
## Post : 객체 이름
### 객체 이름의 첫글자는 무조건 대문자
class Post(models.Model):
    # models : Post가 장고 모델임을 의미
    ##         이 코드 때문에 장고는 Post가 데이터베이스에 저장되어있어야 한다고 안다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # publish(self) : 메서드 이름
    ## 이름을 변경, 붙일때는 공백 대신, 소문자나 언더스코어 사용
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __str__ 주의!(던더라고 불림)
    ## __str__호출하면 Post 모델의 텍스트를 얻게 된다.
    def __str__(self):
        return self.title