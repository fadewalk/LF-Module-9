from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class DemoView(APIView):
    def get(self, request):
        print(request.version)
        print(request.versioning_scheme)
        # 得到版本号  根据版本号的不同返回不同的信息
        if request.version == "v1":
            return Response("v1版本的数据")
        elif request.version == "v2":
            return Response("v2版本的数据")
        return Response("不存在的版本")
