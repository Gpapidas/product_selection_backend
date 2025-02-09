from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock", "created_at", "updated_at")
    search_fields = ("name", "description")
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("-created_at",)


admin.site.register(Product, ProductAdmin)
