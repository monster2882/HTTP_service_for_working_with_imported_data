from django import forms


class UploadForm(forms.Form):
    file_name = forms.CharField(label='Название файла', max_length=255)
    file = forms.FileField(label='Выбрать файл')
