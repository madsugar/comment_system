# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, max_length=1024)

    class Meta:
        model = Comment
        fields = '__all__'
