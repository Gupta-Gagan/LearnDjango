from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions
from .serializer import LikeSerializer
from .models import Likes
from posts.models import Post
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.


class LikePostView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LikeSerializer
    
    def get_queryset(self):
        post_id = self.kwargs['pk']
        return Likes.objects.filter(post_id=post_id)
    
    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, id=post_id)
        like_exists = Likes.objects.filter(user=self.request.user, post=post_id).exists()
        if like_exists:
            raise Exception("You have already liked the post.")
        
        serializer.save(user=self.request.user, post=post)
        
    def delete(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, id=post_id)

        like = Likes.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            print("Like deleted...")
            return Response({"Your Like is Deleted.."})
        

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        like_count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'likes_count': like_count,
            'likes': serializer.data
        })     