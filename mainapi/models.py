from django.db import models

# Create your models here.

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment_title = models.CharField(max_length=100, blank=True, default='')
    comment_body = models.TextField()

    class Meta:
        ordering= ['created']