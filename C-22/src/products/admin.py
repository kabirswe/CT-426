from django.contrib import admin

from .models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_by']
    list_per_page = 20
    ordering = ['name']
    list_display_links = ['name']
