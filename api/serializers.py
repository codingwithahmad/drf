from rest_framework import serializers
from blog.models import Articles
from django.contrib.auth import get_user_model



class ArticleSerializer(serializers.ModelSerializer):
	def get_author(self, obj):
		return obj.author.last_name



	author = serializers.SerializerMethodField("get_author")



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
