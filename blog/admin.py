from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'publish', 'status']
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ['publish', 'status']
    search_fields = ['body', 'title']

admin.site.register(Post, PostAdmin)
