from rest_framework import serializers

from wykop.accounts.serializers import UserSerializer
from wykop.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ('author', )
        fields = ('id', 'url', 'title', 'text', 'image', 'video', 'nsfw', 'author')

    author = UserSerializer(read_only=True)
