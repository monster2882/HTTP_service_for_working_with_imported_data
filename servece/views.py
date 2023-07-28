from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import pandas as pd

from .models import UploadFile
from .forms import UploadForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            file = form.cleaned_data['file']
            uploaded_file = UploadFile(file_name=file_name, file=file)
            uploaded_file.save()
            return redirect('success') 
    else:
        form = UploadForm()
    return render(request, 'servece/upload.html', {'form': form})


def success(request):
    return render(request, 'servece/success.html')
