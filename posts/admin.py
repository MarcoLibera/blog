from django.contrib import admin
from .models import Post, ImagePost

# Class to display ImagePost inline in the Post admin page
class ImagePostInline(admin.TabularInline):
    model = ImagePost
    extra = 1


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImagePostInline]