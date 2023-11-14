from rest_framework import pagination

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = None
    max_page_size = 10
    page_query_param = "pages"