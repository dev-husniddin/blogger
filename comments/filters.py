import django_filters
from .models import Comment

class CommentFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(lookup_expr='icontains')  

    class Meta:
        model = Comment
        fields = ['author']  
