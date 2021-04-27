from django.shortcuts import render
import uuid
from .models import User
from utils.auth import MyAuth
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response


class DemoView(APIView):
    def get(self, request):
        return Response("认证demo~")


class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        pwd = request.data.get("pwd")
        # 登录成功 生成token 会把token给你返回
        token = uuid.uuid4()
        User.objects.create(username=username, pwd=pwd, token=token)
        return Response("创建用户成功")


class TestView(APIView):
    authentication_classes = [MyAuth,]

    def get(self, request):
        print(request.user)
        print(request.auth)
        user_id = request.user.id
        return Response("认证测试")