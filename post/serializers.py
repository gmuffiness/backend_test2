from rest_framework import serializers
from .models import Post, Content

class PostSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(use_url=True)

    class Meta:
        model = Post
        fields = ('title','body','pub_date','target_amount','thumbnail')

class ContentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Content
        fields = ('title','link','image')