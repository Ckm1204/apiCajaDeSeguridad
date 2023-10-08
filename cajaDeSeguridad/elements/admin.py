from django.contrib import admin
from .models import  Secret, Identification, loginKey, card

# Register your models here.
admin.site.register( loginKey)
admin.site.register(card)
admin.site.register(Secret)
admin.site.register(Identification)

