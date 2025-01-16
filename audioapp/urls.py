# audioapp/urls.py

from django.urls import path
from . import views

app_name = 'audioapp'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('upload/', views.upload_page, name='upload_page'),
    path('record/', views.record_page, name='record_page'),
]
