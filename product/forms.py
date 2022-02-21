from django import forms
from .models import ExportalGalleriesFile, ExportalMainPicFile, InternalMainPicFile, InternalGalleriesFile


class ExportalFileForm(forms.ModelForm):
    class Meta:
        model=ExportalGalleriesFile
        fields="__all__"

class InternalFileForm(forms.ModelForm):
    class Meta:
        model=InternalGalleriesFile
        fields="__all__"

class ExportalFileLogoForm(forms.ModelForm):
    class Meta:
        model=ExportalMainPicFile
        fields="__all__"

class InternalFileLogoForm(forms.ModelForm):
    class Meta:
        model=InternalMainPicFile
        fields="__all__"