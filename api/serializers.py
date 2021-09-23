from rest_framework import serializers
from blog.models import Articles
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
>>>>>>> 43a28955ced0486dcb402cdc63b9b44f85bb0701

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articles
		# fields = ("title", "slug", "author", "content", "publish", "status", )
		exclude = ('created', 'updated')

<<<<<<< HEAD
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"
=======
>>>>>>> 43a28955ced0486dcb402cdc63b9b44f85bb0701
