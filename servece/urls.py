from django.urls import path
from .views import *


urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('success/', success, name='success')
]