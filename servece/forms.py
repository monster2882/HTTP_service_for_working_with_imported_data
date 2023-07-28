from django import forms
from django.core.validators import FileExtensionValidator


class UploadForm(forms.Form):
    file_name = forms.CharField(label='Название файла', max_length=255)
    file = forms.FileField(
        label='Выбрать файл',
        validators=[FileExtensionValidator(allowed_extensions=['csv'])]
    )
