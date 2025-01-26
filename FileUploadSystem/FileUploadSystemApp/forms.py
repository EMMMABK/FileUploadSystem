from django import forms

class MyFileUploadForm(forms.Form):
    file_name = forms.CharField(max_length=255)
    files = forms.FileField()