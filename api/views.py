# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
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
from rest_framework.permissions import IsAuthenticated
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


class RevokeToken(APIView):
	permission_classes = (IsAuthenticated, )

	def delete(self, request):
		request.auth.delete()
		return Response(status=204)
