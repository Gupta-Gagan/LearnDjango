from .models import Post
import django_filters

class PostFilters(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    
    class Meta:
        model = Post
        fields = ['title']