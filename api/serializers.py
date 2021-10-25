from rest_framework import serializers
from blog.models import Articles
from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ["id", "username", "first_name", "last_name"]



class ArticleSerializer(serializers.ModelSerializer):
	author = serializers.HyperlinkedIdentityField(view_name="api:author-details")

	class Meta:
		model = Articles
		# fields = ("title", "slug", "author", "content", "publish", "status", )
		exclude = ('created', 'updated')

	def validate_title(self, value):
		filter_list = ["javascript", "laravel", "php"]

		for i in filter_list:
			if i in value:
				raise serializers.ValidationError("Don't use {}".format(i))


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = "__all__"
