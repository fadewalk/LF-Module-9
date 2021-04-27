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

class GenericAPIView(APIView):
    query_set = None
    serializer_class = None

    def get_queryset(self):
        return self.query_set

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)


class ListModelMixin(object):
    def list(self, request):
        queryset = self.get_queryset()
        ret = self.get_serializer(queryset, many=True)
        return Response(ret.data)


class CreateModelMixin(object):
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RetrieveModelMixin(object):
    def retrieve(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        ret = self.get_serializer(book_obj)
        return Response(ret.data)


class UpdateModelMixin(object):
    def update(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        serializer = self.get_serializer(book_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DestroyModelMixin(object):
    def destroy(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        book_obj.delete()
        return Response("")


class ListCreateAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    pass


class RetrieveUpdateDestroyAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass


# class BookView(GenericAPIView, ListModelMixin, CreateModelMixin):
class BookView(ListCreateAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        # book_obj = Book.objects.first()
        # ret = BookSerializer(book_obj)
        # book_list = Book.objects.all()
        # book_list = self.get_queryset()
        # ret = self.get_serializer(book_list, many=True)
        # return Response(ret.data)
        return self.list(request)

    def post(self, request):
        # print(request.data)
        # serializer = BookSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        return self.create(request)


# class BookEditView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
class BookEditView(RetrieveUpdateDestroyAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, id):
        # book_obj = Book.objects.filter(id=id).first()
        # ret = BookSerializer(book_obj)
        # return Response(ret.data)
        return self.retrieve(request, id)

    def put(self, request, id):
        # book_obj = Book.objects.filter(id=id).first()
        # serializer = BookSerializer(book_obj, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        return self.update(request, id)

    def delete(self, request, id):
        # book_obj = Book.objects.filter(id=id).first()
        # book_obj.delete()
        # return Response("")
        return self.destroy(request, id)



# class ViewSetMixin(object):
#     def as_view(self):
#         """
#         按照我们参数指定的去匹配
#         get-->list
#         :return:
#         """


from rest_framework.viewsets import ViewSetMixin


# class ModelViewSet(ViewSetMixin, GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     pass

from rest_framework.viewsets import ModelViewSet


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


from rest_framework import views
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets




















































