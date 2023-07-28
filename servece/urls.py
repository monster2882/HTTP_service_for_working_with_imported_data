from django.urls import path
from .views import *


urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('success/', success, name='success'),
    path('not_success/', not_success, name='not_success'),
    path('api/upload/', UploadFileAPIView.as_view(), name='api_upload_file'),
    path('api/files/', UploadFileAPIView.as_view(), name='api_get_files'),
    path('files/', get_files, name='get_files'),
    path('filter/', view_csv_data, name='filter_csv')
]