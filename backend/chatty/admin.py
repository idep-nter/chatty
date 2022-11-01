from django.contrib import admin

from .models import Thread, Post, Tag

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_tags', 'description']

    def get_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['author', 'thread', 'content']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()