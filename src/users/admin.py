from django.contrib import admin
from .models import Profile,Location


# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    pass

class profileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location,LocationAdmin)
admin.site.register(Profile,profileAdmin)
