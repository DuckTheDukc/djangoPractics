from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name