from django.contrib import admin


from .models import Listing

class ListAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

admin.site.register(Listing,ListAdmin)

