import django_filters
from .models import Comment

class CommentFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(lookup_expr='icontains')  # Фильтр по части имени автора комментария

    class Meta:
        model = Comment
        fields = ['author']  # Указываете поля для фильтрации (можете добавить больше)
