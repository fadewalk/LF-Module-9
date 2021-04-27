# by gaoxin

from django.urls import path
from .views import DemoView, LoginView, TestView


urlpatterns = [
    path(r"", DemoView.as_view()),
    path(r"login", LoginView.as_view()),
    path(r"test", TestView.as_view()),


]