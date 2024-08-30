from rest_framework import serializers
from django.urls import reverse

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('created', 'owner', 'title', 'body')

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep['owner'] = instance.owner.username
        return rep


class PostDetailSerializer(serializers.ModelSerializer):
    comment_set = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'body', 'created', 'updated', 'owner', 'comment_set')

    def to_representation(self, instance):
        rep = super(PostDetailSerializer, self).to_representation(instance)
        rep['owner'] = instance.owner.username
        return rep

    def get_comment_set(self, instance):
        comment_set = []
        for id in Comment.objects.filter(post_id=instance.id).values_list('id', flat=True):
            comment_set.append('http://localhost:8000' + reverse(viewname='comment_detail', kwargs={'pk': id}))
        return comment_set


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'owner', 'body', 'created', 'updated')

    def to_representation(self, instance):
        rep = super(CommentSerializer, self).to_representation(instance)
        rep['owner'] = instance.owner.username
        rep['post'] = 'http://localhost:8000' + reverse(viewname='post_detail', kwargs={'pk': instance.post.id})
        return rep
