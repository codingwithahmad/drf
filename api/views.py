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
	serializer_class = ArticleSerializer


	def get_queryset(self):
		queryset = Articles.objects.all()
		status = self.request.query_params.get('status')
		author = self.request.query_params.get('author')
		

		if status is not None:
			queryset = queryset.filter(status=status)

		if author is not None:
			queryset = queryset.filter(author=author)
		

		return queryset

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

