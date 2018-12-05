from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True)
    body_text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
