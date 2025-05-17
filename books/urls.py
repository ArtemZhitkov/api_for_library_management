from django.urls import path, include
from books.views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", BookViewSet, basename="books")

from books.apps import BooksConfig

app_name = BooksConfig.name

urlpatterns = [
    path("", include(router.urls))
]
