from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
from .models import Post
from .serializers import PostSerializer
from .filters import PostFilters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class PostList(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    pagination_class = LimitOffsetPagination 
    serializer_class = PostSerializer
    filterset_class = PostFilters
    # filter_backends = [DjangoFilterBackend]
    
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    
    serializer_class = PostSerializer
    
    
    
    

