from django.contrib import admin
from .models import Post, Tag

# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    ...
    
@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    ...

