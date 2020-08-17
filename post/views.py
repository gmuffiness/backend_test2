from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world!")

@api_view(['GET'])
def totalPost(request):
    totalPosts = Post.objects.all()
    serializer = PostSerializer(totalPosts, many=True)
    return Response(serializer.data)