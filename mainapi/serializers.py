from rest_framework import serializers
from mainapi.models import Comment

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    comment_title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    comment_body = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Comment.objects.create(**validated_data)

    def update(self,instance, validated_data):
        instance.comment_title = validated_data.get('comment_title', instance.comment_title)
        instance.comment_body = validated_data.get('comment_body', instance.comment_body)
        instance.save()
        return instance