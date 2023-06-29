from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.

admin.site.register(Category)


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'category',  'time_added')


admin.site.register(Post, AdminPost)


class AdminComment(admin.ModelAdmin):
    list_display = ('post', 'email', 'content', 'status')


admin.site.register(Comment, AdminComment)
