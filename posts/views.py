from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
from .models import Post
from .serializers import PostSerializer
from .filters import PostFilters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

# Create your views here.

class PostList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    pagination_class = LimitOffsetPagination 
    serializer_class = PostSerializer
    filterset_class = PostFilters
    
    def create(self, request, *args, **kwargs):
        is_bulk = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_bulk)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save()
    
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    
    serializer_class = PostSerializer
    
    
    
    

