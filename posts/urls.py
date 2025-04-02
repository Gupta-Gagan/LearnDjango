from django.urls import path,include
from .views import PostList, PostDetail

urlpatterns = [
    
    path('', PostList.as_view()),
    path('/<int:pk>/', PostDetail.as_view()),
    path('/<int:pk>/comments/', include('comments.urls')),
    path('/<int:pk>/likes/', include('likes.urls'))
]