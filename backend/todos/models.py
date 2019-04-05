from django.db import models
from django.urls import reverse
from django.utils import timezone


class TodoList(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def incomplete_items(self):
        return self.todo_items.filter(complete=False).order_by("-assigned_date")

    def complete_items(self):
        return self.todo_items.filter(complete=True).order_by("-complete_date")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("todo_list_detail", kwargs={"pk": self.pk})
    
class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, related_name="todo_items" ,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500)
    item_detail = models.TextField(blank=True, null=True)
    assigned_date = models.DateTimeField(default=timezone.now())
    complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)

    def mark_completed(self):
        self.complete = True
        self.complete_date = timezone.now()
        self.save()

    def mark_not_completed(self):
        self.complete = False
        self.complete_date = None
        self.save()
        

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("todo_list_detail", kwargs={"pk": self.todo_list.pk})
    