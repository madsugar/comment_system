from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.
import logging

from django import forms

logger = logging.getLogger(__name__)


class CommentUpdateForm(forms.Form):
    comment = forms.Textarea()

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            user = "anonymous"
        else:
            user = request.user.last_name

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = serializer.instance
        instance.user = user
        instance.save()
        serializer = self.get_serializer(instance=instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




