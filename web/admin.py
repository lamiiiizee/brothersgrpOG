from django.contrib import admin

from .models import Contact
from .models import Sector
from .models import Update, SectorFeature, Client



admin.site.register(Contact)
admin.site.register(Update)


class SectorFeatureInline(admin.TabularInline):
    model = SectorFeature
    extra = 1


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [SectorFeatureInline,]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
