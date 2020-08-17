from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField() # 추후 콘텐츠에 따라 수정 예정
    pub_date = models.DateTimeField('date published')
    target_amount = models.IntegerField(default=10000)
    thumbnail = models.ImageField(default='test_img.jpg')
    
    def __str__(self):
        return self.title

    # def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Content(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField()
    image = models.ImageField(default='test_img.jpg')
