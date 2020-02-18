from django.contrib import admin
from .models import Post, Comments


class CommentsInline(admin.TabularInline):
    model = Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('author', )
        }),
        ('Context', {
            'fields': ('title', 'text', 'post_likes')
        }),
        ("Data", {
            'fields': ('created_date', 'published_date')
        }),
    )

    inlines = [CommentsInline, ]
