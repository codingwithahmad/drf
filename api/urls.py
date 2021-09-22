from django.urls import path
from .views import ArticlesList

app_name = "api"

urlpatterns = [
	path("", ArticlesList.as_view(), name="list"),
]