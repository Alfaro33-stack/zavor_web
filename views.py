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
            'huariques_count': '120+',
            'active_neighbors': '4.8k',
            'rating_average': '4.9/5',
            'downloads': '12.5k'
        },
        'featured_places': [
            {
                'name': 'Pollería El Gordo de la Central',
                'category': 'Pollerías',
                'badge': 'Top Vecino',
                'rating': '4.9 ★',
                'location': 'Av. Central Mz. B Lt. 14, VES',
                'desc': 'El verdadero pollo al grano con ají de huacatay artesanal insuperable.',
                'tag': 'Populares',
                'image': 'images/pollo_brasa.png'
            },
            {
                'name': 'Cebichería Mi Rico Puerto',
                'category': 'Mariscos & Cebiches',
                'badge': 'Recomendado',
                'rating': '4.8 ★',
                'location': 'Sector 2 Grupo 15, Villa El Salvador',
                'desc': 'Cebiche de pesca del día con chicharrón de pota súper crocante.',
                'tag': 'Huarique Oculto',
                'image': 'images/ceviche.png'
            },
            {
                'name': 'Anticuchos Doña Jacinta',
                'category': 'Nocturnos & Brasas',
                'badge': 'Tradición',
                'rating': '5.0 ★',
                'location': 'Av. Revolución cruzando con Av. Lima',
                'desc': 'Corazón tierno sazonado con receta secreta de más de 25 años.',
                'tag': 'Nocturno',
                'image': 'images/anticuchos.png'
            }
        ],
        'reviews': [
            {
                'author': 'Carlos Mendoza',
                'role': 'Vecino de Sector 3',
                'comment': '¡Al fin una app que conoce los verdaderos huariques de VES! Encontré una cebichería oculta a dos cuadras de mi casa que no aparecía en Google Maps.',
                'rating': 5
            },
            {
                'author': 'Rosa Huamán',
                'role': 'Dueña de "El Sabor del Parque"',
                'comment': 'Zavor nos ayudó a llenar las mesas los fines de semana sin pagar comisiones absurdas de delivery. Los clientes llegan directo por el mapa.',
                'rating': 5
            },
            {
                'author': 'Javier Ruiz',
                'role': 'Gastrónomo Urbano',
                'comment': 'La app corre súper fluida y descargar el APK directamente desde aquí fue facilísimo. Muy recomendada para los foodies del cono sur.',
                'rating': 5
            }
        ]
    }
    return render(request, 'landing/index.html', context)

def download_apk(request):
    """
    Vista encargada de redireccionar a la descarga del APK directamente desde Firebase Storage.
    """
    firebase_apk_url = "https://firebasestorage.googleapis.com/v0/b/zavor-fe238.firebasestorage.app/o/app%2FZavoR.apk?alt=media&token=90d69524-8611-4a3b-af6b-e96f00d935e3"
    return redirect(firebase_apk_url)
