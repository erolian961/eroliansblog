from django.contrib import admin
from blog.models import Category, Tag, Post, ContentImage
from django_summernote.admin import SummernoteModelAdmin
from .models import QuillPost

class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInline,
    ]
    summernote_fields = '__all__'



admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass
