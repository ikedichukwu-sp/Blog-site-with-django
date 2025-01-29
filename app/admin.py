from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Article, UserProfile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "word_count", "status", "created_at", "updated_at")  # Add this line to display fields
    list_filter = ("title", "word_count", "status", "created_at", "updated_at")
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
    readonly_fields = ("word_count", "created_at", "updated_at")


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),  # this makes the field a bit wider
            "fields": ("email", "password1", "password2")}),
    )
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile, CustomUserAdmin)
