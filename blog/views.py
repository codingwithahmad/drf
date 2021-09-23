from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Articles
# Create your views here.

class ArticleList(ListView):
	def get_queryset(self):
		return Articles.objects.filter(status=True)


class ArticleDetail(DetailView):
	def get_object(self):
		return get_object_or_404(
			Articles.objects.filter(status=True),
		 	slug=self.kwargs.get('slug'),
		)