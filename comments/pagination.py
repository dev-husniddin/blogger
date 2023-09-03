from rest_framework.pagination import PageNumberPagination

class CommentPagination(PageNumberPagination):
    page_size = 10  # Количество комментариев на странице
    page_size_query_param = 'page_size'
    max_page_size = 100  # Максимальное количество комментариев на странице
