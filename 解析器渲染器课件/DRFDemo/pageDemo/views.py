from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from SerDemo.models import Book
from SerDemo.serializers import BookSerializer

# Create your views here.
from rest_framework import pagination
from utils.pagination import MyPagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin


# class BookView(APIView):
#
#     def get(self, request):
#         queryset = Book.objects.all()
#         # 1,实例化分页器对象
#         page_obj = MyPagination()
#         # 2，调用分页方法去分页queryset
#         page_queryset = page_obj.paginate_queryset(queryset, request, view=self)
#         # 3，把分页好的数据序列化返回
#         # 4, 带着上一页下一页连接的响应
#         ser_obj = BookSerializer(page_queryset, many=True)
#
#         return page_obj.get_paginated_response(ser_obj.data)


class BookView(GenericAPIView, ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = MyPagination
    # self.paginate_queryset(queryset)

    def get(self, request):
        return self.list(request)
