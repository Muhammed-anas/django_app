from django.contrib import admin
from .models import profile,Location


# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    pass

class profileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location,LocationAdmin)
admin.site.register(profile,profileAdmin)
