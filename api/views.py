# from django.shortcuts import render
from blog.models import Articles
<<<<<<< HEAD
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import (
	
	ListAPIView, 
	
	ListCreateAPIView, 
	
	RetrieveDestroyAPIView, 
	
	RetrieveUpdateAPIView,
)
=======
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView
>>>>>>> 43a28955ced0486dcb402cdc63b9b44f85bb0701
# Create your views here.
class ArticlesList(ListCreateAPIView):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer
<<<<<<< HEAD


class ArticlesDetail(RetrieveDestroyAPIView):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'slug'



class UserList(ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(RetrieveDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserUpdate(RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
=======
>>>>>>> 43a28955ced0486dcb402cdc63b9b44f85bb0701
