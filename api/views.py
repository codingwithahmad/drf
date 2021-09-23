# from django.shortcuts import render
from blog.models import Articles
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import (
	
	ListAPIView, 
	
	ListCreateAPIView, 
	
	RetrieveDestroyAPIView, 
	
	RetrieveUpdateAPIView,
)
# Create your views here.
class ArticlesList(ListCreateAPIView):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer


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