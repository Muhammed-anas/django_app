from django.contrib import admin


from .models import Listing

class ListAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listing,ListAdmin)

