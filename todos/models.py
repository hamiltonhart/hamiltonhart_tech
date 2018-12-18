from django.db import models
from django.urls import reverse
from django.utils import timezone


class TodoList(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def incomplete_items(self):
        return self.todo_items.filter(complete_item=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("todo_list_detail", kwargs={"pk": self.pk})
    
class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, related_name="todo_items" ,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500)
    item_detail = models.TextField(blank=True, null=True)
    assigned_date = models.DateTimeField(default=timezone.now())
    complete_item = models.BooleanField(default=False)
    complete_date = models.DateTimeField(blank=True, null=True)

    def mark_completed(self):
        self.complete_item = True
        self.complete_date = timezone.now()
        self.save()

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("todo_list_detail", kwargs={"pk": self.todo_list.pk})
    