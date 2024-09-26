from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    # Fields that are read-only in the admin interface
    readonly_fields = (
        'name',
        'email',
        'subject',
        'message',
        'created_at'
    )
    # Fields displayed on the Contact form in the admin
    fields = (
        'name',
        'email',
        'subject',
        'message',
        'created_at',
        'resolved',
    )
    # Fields shown in the list view of the Contact entries
    list_display = (
        'email',
        'created_at',
        'resolved'
    )
    # Orders contacts by creation date, most recent first
    ordering = ('-created_at',)


admin.site.register(Contact, ContactAdmin)
