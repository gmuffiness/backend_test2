from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Content

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'pub_date', 'target_amount','thumbnail']
    list_display_links = ['id', 'title']

    # def content_size(self, post):
        # return mark_safe('<u>{}</u>글자'.format(len(post.body)))
    # content_size.short_description = '글자수'
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'link','image']
    list_display_links = ['id', 'title']