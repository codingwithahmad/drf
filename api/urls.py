from django.urls import path, include
from .views import UserViewSet, ArticleViewSet, AuthorRetrieve
from rest_framework import routers

app_name = "api"

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet, basename="articles")
router.register('users', UserViewSet, basename="users")

# urlpatterns = router.urls

urlpatterns = [
	path("", include(router.urls)),
	path("authors/<int:pk>", AuthorRetrieve.as_view(), name="author-details")
]