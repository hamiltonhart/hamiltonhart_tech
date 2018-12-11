from django.db import models
from django.urls import reverse


class TodoList(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def incomplete_item(self):
        return self.todo_items.filter(incomplete_item=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("todo_list_detail", kwargs={"pk": self.pk})
    
class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, related_name="todo_items" ,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500)
    incomplete_item = models.BooleanField(default=True)

    def mark_completed(self):
        self.incomplete_item = False
        self.save()

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("todo_list_detail", kwargs={"pk": self.todo_list.pk})
    