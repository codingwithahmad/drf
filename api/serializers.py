from rest_framework import serializers
from blog.models import Articles

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articles
		# fields = ("title", "slug", "author", "content", "publish", "status", )
		exclude = ('created', 'updated')

