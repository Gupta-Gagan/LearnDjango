from django.contrib import admin
from django.urls import path, include
from comments.views import CommentList, CommentDetails

urlpatterns = [
    path('',CommentList.as_view()),
    path('<int:pk>/', CommentDetails.as_view()),
]

