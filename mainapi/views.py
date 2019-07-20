from django.shortcuts import render
from rest_framework import viewsets
from mainapi.models import Comment
from mainapi.serializers import CommentSerializer
# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer