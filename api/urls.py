from django.urls import path
from .views import ArticlesList, ArticlesDetail, UserList, UserDetail, UserUpdate
from .views import ArticlesList


app_name = "api"

urlpatterns = [
	path("", ArticlesList.as_view(), name="list"),
	path("<slug:slug>", ArticlesDetail.as_view(), name="detail"),
	path("users/", UserList.as_view(), name="user-list"),
	path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
	path("users/update/<int:pk>", UserUpdate.as_view(), name="user-update"),
	


]