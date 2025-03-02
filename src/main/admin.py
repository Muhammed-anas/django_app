from django.contrib import admin


from .models import Listing, LikedListing

class ListAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    
class likedAdmin(admin.ModelAdmin):
    pass

admin.site.register(LikedListing,likedAdmin)
admin.site.register(Listing,ListAdmin)

