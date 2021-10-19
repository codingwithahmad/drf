from blog.models import Articles
from django.contrib.auth import get_user_model
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import (
 
	IsAuthorOrReadOnly, 

	IsStaffOrReadOnly,

	IsSuperUserOrStaffReadOnly,
)
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer
# Create your views here.



class ArticleViewSet(ModelViewSet):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer
	filterset_fields = ['status', 'author__username']
	search_fields = [
		"title", 
		"content",  
		"author__username",
		"author__first_name", 
	 	"author__last_name",
	]

	ordering = ["-publish"]
	ordering_fields = [
		"publish",
		"status",
	]

	def get_permissions(self):
		if self.action in ['list', 'create']:
			permission_classes = (IsStaffOrReadOnly, )
		else:
			permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

		return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperUserOrStaffReadOnly, )

