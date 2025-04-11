from django import forms
from .models import SchemeReport

class SchemeReportForm(forms.ModelForm):
    class Meta:
        model = SchemeReport
        fields = ['description', 'location', 'category', 'evidence']