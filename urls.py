from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.home, name='home'),
    path('descargar/', views.download_apk, name='download_apk'),
]
