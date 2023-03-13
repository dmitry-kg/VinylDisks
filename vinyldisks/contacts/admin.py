from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'text' )
    list_display_link = ('first_name', 'email', 'text')
    search_fields = ('first_name', 'email', 'theme')
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)