from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Listings, Bid, User, ListingComment, Categories, WatchList

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Listings)
admin.site.register(Bid)
admin.site.register(ListingComment)
admin.site.register(Categories)
admin.site.register(WatchList)