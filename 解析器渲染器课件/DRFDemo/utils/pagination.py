# by gaoxin
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


# class MyPagination(PageNumberPagination):
#     # xxxx?page=1&size=2
#     page_size = 1
#     page_query_param = "page"
#     page_size_query_param = "size"
#     max_page_size = 3



# class MyPagination(LimitOffsetPagination):
#
#     default_limit = 1
#     limit_query_param = "limit"
#     offset_query_param = "offset"
#     max_limit = 3



class MyPagination(CursorPagination):

    cursor_query_param = "cursor"
    page_size = 2
    ordering = "-id"






