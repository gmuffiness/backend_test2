from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world!")

@api_view(['GET'])
def totalPost(request):
    totalPosts = Post.objects.all()
    serializer = PostSerializer(totalPosts, many=True)
    return Response(serializer.data)

def home(request):
    posts = Post.objects
    return render(request, 'post/home.html', {'posts':posts})

def kakaopayment(request):
    posts = Post.objects
    return render(request, 'post/kakaopayment.html', {'posts':posts})