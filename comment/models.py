from django.db import models


# Create your models here.
class Comment(models.Model):
    topic = models.CharField(max_length=50)
    user = models.CharField(max_length=1024)
    comment = models.TextField(default="", blank="")
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

