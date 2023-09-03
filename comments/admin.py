from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at',)
    list_filter = ('author', 'post',)
    search_fields = ('author__nickname', 'post__title',)
