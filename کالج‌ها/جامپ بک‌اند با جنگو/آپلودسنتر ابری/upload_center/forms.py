from django import forms


class UploadFileForm(forms.Form):
    file_name = forms.CharField(min_length=3, max_length=30)
    file = forms.FileField()
