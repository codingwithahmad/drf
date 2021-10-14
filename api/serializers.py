from rest_framework import serializers
from blog.models import Articles
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articles
		# fields = ("title", "slug", "author", "content", "publish", "status", )
		exclude = ('created', 'updated')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = "__all__"
