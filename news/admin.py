from django.contrib import admin
from .models import Category, Post, Comment, Tag
# Register your models here.


class AdminCategory(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated')
    list_filter = ['date_created', 'date_updated']
    search_fields = ['title']


admin.site.register(Category, AdminCategory)


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'category',  'time_added')
    list_filter = ['category', 'time_added', 'tags']
    search_fields = ['title']


admin.site.register(Post, AdminPost)


class AdminComment(admin.ModelAdmin):
    list_display = ('title', 'post', 'email', 'content', 'status')
    list_filter = ['status', 'post']
    search_fields = ['post__title', 'title']


admin.site.register(Comment, AdminComment)


class AdminTag(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    list_filter = ['date_created']
    search_fields = ['title']


admin.site.register(Tag, AdminTag)
