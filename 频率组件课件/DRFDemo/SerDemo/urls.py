# by gaoxin
from django.urls import path, include
from .views import BookView, BookEditView, BookModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r"$", BookModelViewSet)


urlpatterns = [
    # path('list', BookView.as_view()),
    # path('retrieve/<int:id>', BookEditView.as_view()),
    # path('list', BookModelViewSet.as_view({"get": "list", "post": "create"})),
    # path('retrieve/<int:pk>', BookModelViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

]


urlpatterns += router.urls










