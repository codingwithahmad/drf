# from django.shortcuts import render
from blog.models import Articles
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserSerializer
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
from rest_framework.permissions import IsAdminUser
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView
# Create your views here.
class ArticlesList(ListCreateAPIView):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer


class ArticlesDetail(RetrieveUpdateDestroyAPIView):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'slug'
	permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)



class UserList(ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperUserOrStaffReadOnly, )


class UserDetail(RetrieveDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperUserOrStaffReadOnly, )

class UserUpdate(RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperUserOrStaffReadOnly, )
