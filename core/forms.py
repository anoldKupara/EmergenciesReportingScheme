from django import forms
from .models import SchemeReport
from django import forms
from .models import SchemeReport, CounselingRequest

class SchemeReportForm(forms.ModelForm):
    class Meta:
        model = SchemeReport
        fields = ['description', 'location', 'category', 'evidence']

class CounselingRequestForm(forms.ModelForm):
    class Meta:
        model = CounselingRequest
        fields = ['message']

class SchemeReportForm(forms.ModelForm):
    class Meta:
        model = SchemeReport
        fields = ['description', 'location', 'category', 'evidence']