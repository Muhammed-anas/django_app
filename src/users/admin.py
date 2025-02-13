from django.contrib import admin
from .models import profile


# Register your models here.

class profileAdmin(admin.ModelAdmin):
    pass

admin.site.register(profile,profileAdmin)
