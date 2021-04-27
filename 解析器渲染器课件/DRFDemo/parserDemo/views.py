from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework import parsers

# Create your views here.


class DjangoView(View):
    def get(self, request):
        print(type(request))
        # Request
        # request.GET
        # request.POST
        # json request.body
        return HttpResponse("django解析器测试~~")


class DRFView(APIView):
    parser_classes = [parsers.JSONParser, ]

    def get(self, request):
        # request 重新封装的request  Request
        # request.data
        #
        return Response("DRF解析器的测试~~")

