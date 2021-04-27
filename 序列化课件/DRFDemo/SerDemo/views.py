from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Book, Publisher
import json


from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from .serializers import BookSerializer


# Create your views here.
# book_list = [
#     {
#         "id": 1,
#         "title": "xxx",
#         .....
#     },
#     {
#
#     }
# ]


# class BookView(View):
#
#     # 第一版 用.values JsonResponse实现序列化
#     # def get(self, request):
#     #     book_list = Book.objects.values("id", "title", "category", "pub_time", "publisher")
#     #     book_list = list(book_list)
#     #     ret = []
#     #     for book in book_list:
#     #         publisher_id = book["publisher"]
#     #         publisher_obj = Publisher.objects.filter(id=publisher_id).first()
#     #         book["publisher"] = {
#     #             "id": publisher_id,
#     #             "title": publisher_obj.title
#     #         }
#     #         ret.append(book)
#     #     # ret = json.dumps(book_list, ensure_ascii=False)
#     #     return JsonResponse(ret, safe=False, json_dumps_params={"ensure_ascii": False})
#
#     # 第二版 用django serializers实现序列化
#     # def get(self, request):
#     #     book_list = Book.objects.all()
#     #     ret = serializers.serialize("json", book_list, ensure_ascii=False)
#     #     return HttpResponse(ret)


class BookView(APIView):

    def get(self, request):
        # book_obj = Book.objects.first()
        # ret = BookSerializer(book_obj)
        book_list = Book.objects.all()
        ret = BookSerializer(book_list, many=True)
        return Response(ret.data)


    def post(self, request):
        print(request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class BookEditView(APIView):

    def get(self, request, id):
        book_obj = Book.objects.filter(id=id).first()
        ret = BookSerializer(book_obj)
        return Response(ret.data)
      
    def put(self, request, id):
        book_obj = Book.objects.filter(id=id).first()
        serializer = BookSerializer(book_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        book_obj = Book.objects.filter(id=id).first()
        book_obj.delete()
        return Response("")























































