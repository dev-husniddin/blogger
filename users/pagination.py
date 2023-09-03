from rest_framework.pagination import PageNumberPagination

class UserPagination(PageNumberPagination):
    page_size = 10  # Количество пользователей на странице
    page_size_query_param = 'page_size'
    max_page_size = 100  # Максимальное количество пользователей на странице
