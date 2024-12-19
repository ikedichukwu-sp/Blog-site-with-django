from django.contrib import admin
from app.models import Article, UserProfile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "word_count", "status", "created_at", "updated_at")  # Add this line to display fields
    list_filter = ("title", "word_count", "status", "created_at", "updated_at")
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
    readonly_fields = ("word_count", "created_at", "updated_at")



admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile)
