from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 20
    page_query_param = "page"
    page_size_query_param = "limit"
