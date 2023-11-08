from django.db import models
from users.models import MyUser

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    parent_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.category_name

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    topic_id = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
