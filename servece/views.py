from django.http import JsonResponse, HttpResponse, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
import pandas as pd
from django.urls import reverse
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UploadFileSerializer
from .models import UploadFile
from .forms import UploadForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            file = form.cleaned_data['file']
            uploaded_file = UploadFile(file_name=file_name, file=f'C:/Users/User/django/test/http_servece/media{file}')
            uploaded_file.save()
            return redirect('success')
        else:
            return redirect('not_success')
    else:
        form = UploadForm()
    return render(request, 'servece/upload.html', {'form': form})


def success(request):
    return render(request, 'servece/success.html')


def not_success(request):
    return render(request, 'servece/not_success.html')


def get_files(request):
    files = UploadFile.objects.all()
    file_data = UploadFileSerializer(files, many=True).data
    return render(request, 'servece/file_list.html', {'files': file_data})


def get_csv_data(csv_file_path, filters=None, sort_columns=None, columns=None):
    df = pd.read_csv(csv_file_path)

    if filters:
        for filter_str in filters:
            df = df.query(filter_str)

    if sort_columns:
        df.sort_values(by=sort_columns, inplace=True)

    if columns:
        df = df[columns]

    return df


def view_csv_data(request):
    csv_file_path = ''
    filters = [""]
    sort_columns = [""]
    columns = [""]

    df = get_csv_data(csv_file_path, filters=filters, sort_columns=sort_columns, columns=columns)

    return render(request, 'csv_data.html', {'csv_data': df.to_html()})


class UploadFileAPIView(APIView):
    parser_classes = [FileUploadParser]

    @staticmethod
    def post( request):
        file_serializer = UploadFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response({'message': 'Файл успешно загружен'}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        files = UploadFile.objects.all()
        file_data = UploadFileSerializer(files, many=True).data
        return Response(file_data, status=status.HTTP_200_OK)


