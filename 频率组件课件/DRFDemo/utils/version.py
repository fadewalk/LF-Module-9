# by gaoxin
from rest_framework import versioning


class MyVersion(object):
    def determine_version(self, request, *args, **kwargs):
        # 返回值 给了request.version
        # 返回版本号
        # 版本号携带在过滤条件 xxxx?version=v1
        version = request.query_params.get("version", "v1")

        return version