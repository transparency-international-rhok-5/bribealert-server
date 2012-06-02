from django.contrib import admin

from models import Bribe

class BribeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bribe, BribeAdmin)