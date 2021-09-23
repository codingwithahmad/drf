from django.urls import path
<<<<<<< HEAD
from .views import ArticlesList, ArticlesDetail, UserList, UserDetail, UserUpdate
=======
from .views import ArticlesList
>>>>>>> 43a28955ced0486dcb402cdc63b9b44f85bb0701

app_name = "api"

urlpatterns = [
	path("", ArticlesList.as_view(), name="list"),
<<<<<<< HEAD
	path("<slug:slug>", ArticlesDetail.as_view(), name="detail"),
	path("users", UserList.as_view(), name="user-list"),
	path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
	path("users/update/<int:pk>", UserUpdate.as_view(), name="user-update"),
	
=======
>>>>>>> 43a28955ced0486dcb402cdc63b9b44f85bb0701
]