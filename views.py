import os
from io import BytesIO
from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render, redirect

def home(request):
    """
    Renderiza la Landing Page de Zavor con contexto dinamico y promocional.
    """
    context = {
        'app_name': 'ZavoR',
        'district': 'Villa El Salvador',
        'version': '1.0.4',
        'stats': {
            'huariques_count': '50+',
            'active_neighbors': '0%',
            'rating_average': '100%',
    }
    return render(request, 'landing/index.html', context)

def download_apk(request):
    """
    Vista encargada de redireccionar a la descarga del APK directamente desde Firebase Storage.
    """
    firebase_apk_url = "https://firebasestorage.googleapis.com/v0/b/zavor-fe238.firebasestorage.app/o/app%2FZavoR.apk?alt=media&token=0eb9a994-aa87-436d-93e8-aa8019c175c8"
    return redirect(firebase_apk_url)
