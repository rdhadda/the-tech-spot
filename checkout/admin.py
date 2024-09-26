from django.contrib import admin
from .models import Order, OrderLineItem


# Admin for displaying OrderLineItems within the Order admin
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    # Fields that are automatically generated and not editable by the admin
    # user
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid')
    # Fields to display on the Order form in the admin interface
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 'stripe_pid')
    # Fields to display in the list view of orders in the admin panel
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    # Orders are displayed by date in descending order
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
