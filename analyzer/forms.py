from django import forms
from django.utils.translation import gettext as _

from analyzer.models import AnalyzeImage


class AnalyzeImageForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
        'name': 'file',
        'accept': 'image/*',
        'required': '',
        'multiple': '',
    }))
    range_picker = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'hidden',
        'class': 'range-picker',
        'value': '50',
        'style': 'display: none;',
    }))
    color_picker_h = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'hidden',
        'class': 'range-slider-h',
        'value': '120,175',
        'style': 'display: none;',
    }))
    color_picker_s = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'hidden',
        'class': 'range-slider-s',
        'value': '80,255',
        'style': 'display: none;',
    }))
    color_picker_v = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'hidden',
        'class': 'range-slider-v',
        'value': '50,255',
        'style': 'display: none;',
    }))

    class Meta:
        model = AnalyzeImage
        fields = ("file", "range_picker", "color_picker_h",
                  "color_picker_s", "color_picker_v")
