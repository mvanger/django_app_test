from django.contrib import admin

# Register your models here.
from weblog.models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'pub_date']

admin.site.register(Post, PostAdmin)