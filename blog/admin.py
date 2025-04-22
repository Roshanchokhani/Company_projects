from django.contrib import admin
from .models import Post

 
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'created_at') 
    list_filter = ('published_at', 'created_at', 'author') 
    search_fields = ('title', 'content') 
    
    date_hierarchy = 'published_at' 
    ordering = ('-published_at', '-created_at') 

admin.site.register(Post)

