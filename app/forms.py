from django import forms
from app.models import *
from django.template.loader import render_to_string
from django.forms import widgets
from django.utils.safestring import mark_safe


class LocationWidget(widgets.TextInput):
    """Map Widget"""
    template_name = 'draw.html'
    def render(self, name, value, attrs=None):
    	context = {'POLYGON':value}
        return mark_safe(render_to_string(self.template_name, context))



class CityFrom(forms.ModelForm):
    """City Form"""
    shape = forms.CharField(widget = LocationWidget())
    class Meta:
        model = City
        fields = "__all__"