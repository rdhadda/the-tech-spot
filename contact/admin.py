from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'email',
        'subject',
        'message',
        'created_at'
    )

    fields = (
        'name',
        'email',
        'subject',
        'message',
        'created_at',
        'resolved',  
    )

    list_display = (
        'email',
        'created_at',
        'resolved'
    )

    ordering = ('-created_at',)


admin.site.register(Contact, ContactAdmin)

