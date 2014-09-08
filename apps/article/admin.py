from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from apps.article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumb_display', 'content_display']
    search_fields = ['title', 'content']

    def content_display(self, obj):
        return mark_safe(Truncator(obj.content).words(30, html=True, truncate=' see more'))
    content_display.short_description = 'Content'
    content_display.admin_order_field = 'content'

    def thumb_display(self, obj):
    	return mark_safe(u'<img src="/static/media/%s" />' % obj.image)
    thumb_display.short_description = 'Image'
    thumb_display.admin_order_field = 'image_thumb'
    # thumb_display.allow_tags = True

# Register your models here.
admin.site.register(Article, ArticleAdmin)
