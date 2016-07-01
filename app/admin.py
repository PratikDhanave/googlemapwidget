from django.contrib.gis import admin
from app.models import *
from app.forms import *


class CityAdmin(admin.ModelAdmin):
    """Display panel of CityAdmin Model"""
    form = CityFrom 
    model = City
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(City, CityAdmin)
