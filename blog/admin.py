from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    list_filter = ("author",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'commented_on')
    list_filter = ("post",)
  
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)