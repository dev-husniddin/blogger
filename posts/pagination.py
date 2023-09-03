from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    page_size = 10  # Количество постов на странице
    page_size_query_param = 'page_size'
    max_page_size = 100  # Максимальное количество постов на странице
