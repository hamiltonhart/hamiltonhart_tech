from django.db import models

from blog.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract=True

class PostTag(Tag):
    posts = models.ManyToManyField(Post, related_name="tags", blank=True, null=True)

