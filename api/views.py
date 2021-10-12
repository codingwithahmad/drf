from blog.models import Articles
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.viewsets import ModelViewset
from rest_framework.generics import (
	
	ListAPIView, 
	
	ListCreateAPIView, 
	
	RetrieveDestroyAPIView, 
	
	RetrieveUpdateAPIView,

	RetrieveUpdateDestroyAPIView,
)
from .permissions import (
 
	IsAuthorOrReadOnly, 

	IsStaffOrReadOnly,

	IsSuperUserOrStaffReadOnly,
)
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView
# Create your views here.



class ArticleViewSet(ModelViewset):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer


	def get_permissions(self):
		if self.action in ['list', 'create']:
			permission_classes = (IsStaffOrReadOnly, )
		else:
			permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

		return [permissions() for permission in permission_classes]


class UserViewSet(ModelViewset):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperUserOrStaffReadOnly, )

