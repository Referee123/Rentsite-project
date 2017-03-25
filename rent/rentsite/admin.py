from django.contrib import admin
from rentsite.models import Apartament


# Register your models here.
class ApartamentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']


admin.site.register(Apartament, ApartamentAdmin)