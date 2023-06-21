from django.db import models

# Create your models here.
class Post(models.Model):
    # 데이터베이스의 필드(컬럼): 최대 길이가 30
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author는 추후 작성
    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'