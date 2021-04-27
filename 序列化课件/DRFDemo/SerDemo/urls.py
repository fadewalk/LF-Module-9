# by gaoxin
from django.urls import path, include
from .views import BookView, BookEditView


urlpatterns = [
    path('list', BookView.as_view()),
    path('retrieve/<int:id>', BookEditView.as_view()),


]