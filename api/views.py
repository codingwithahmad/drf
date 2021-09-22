# from django.shortcuts import render
from blog.models import Articles
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView
# Create your views here.
class ArticlesList(ListCreateAPIView):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer
