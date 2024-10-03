from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """ Displays these fields within the Django
     admin login
    """
    # Fields shown in the list view of the Contact entries
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    # order all the products via their SKU number
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """ Displays these fields within the Django
     admin login
    """
    # Fields shown in the list view of the Contact entries
    list_display = (
        'friendly_name',
        'name'
    )


class ReviewAdmin(admin.ModelAdmin):
    """ Displays these fields within the Django
     admin login
    """
    list_display = (
        'product',
        'user',
        'rating',
        'review',
        'created_at'
    )

    ordering = ('-created_at',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
