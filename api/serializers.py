from rest_framework import serializers
from blog.models import Articles
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articles
		# fields = ("title", "slug", "author", "content", "publish", "status", )
		exclude = ('created', 'updated')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"
