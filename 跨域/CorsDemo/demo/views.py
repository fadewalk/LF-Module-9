from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class DemoView(APIView):
    def get(self, request):
        res = "handlerResponse('跨域测试')"
        return HttpResponse(res)

    def put(self, request):
        return Response("put接口测试")

    def post(self, request):
        return Response("POST接口测试")