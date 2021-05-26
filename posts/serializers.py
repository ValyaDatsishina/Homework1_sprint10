from rest_framework import serializers
from .models import Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date',)
        model = Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username',)
        model = User
