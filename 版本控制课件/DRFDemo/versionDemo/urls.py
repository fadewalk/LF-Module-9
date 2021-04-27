# by gaoxin

from django.urls import path, include
from .views import DemoView


urlpatterns = [
    path(r"", DemoView.as_view()),


]