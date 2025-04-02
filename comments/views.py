from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Comments
from rest_framework.pagination import LimitOffsetPagination
from .serializer import CommentSerializer
from rest_framework.exceptions import PermissionDenied

# Create your views here.

class CommentList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        post_id = self.kwargs['pk']
        return Comments.objects.filter(pk=post_id)
    

class CommentDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    
    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            print("Permission denied.....")
            raise PermissionDenied("You can only edit your own comments")
        serializer.save()
    
    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            print("You are not authorized to delete your comments")
            raise PermissionDenied("You can only delete your own comments")
        instance.delete()
    
