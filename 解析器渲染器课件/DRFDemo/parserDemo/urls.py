# by gaoxin

from django.urls import path, include
from .views import DjangoView, DRFView


urlpatterns = [
    path('demo', DjangoView.as_view()),
    path('test', DRFView.as_view()),


]

