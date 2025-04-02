from django.contrib import admin
from django.urls import path
from likes.views import LikePostView

urlpatterns = [
    path('',LikePostView.as_view()),
]