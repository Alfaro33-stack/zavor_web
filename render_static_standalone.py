import os
import django
from django.conf import settings
from django.template import Context, Engine

# Definir el contexto tal cual está en views.py
context_dict = {
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

def render_standalone():
    # Setup minimal Django settings
    if not settings.configured:
        settings.configure(
            TEMPLATES=[{
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(os.getcwd(), 'templates')],
            }]
        )
    django.setup()

    # Create an engine and load the template
    engine = Engine.get_default()
    
    # Custom tags handling:
    # Since we removed the app, we can just pre-process the HTML file to remove {% load static %}
    # and change {% static 'path' %} to {{ STATIC_URL }}path
    # Let's read index.html from root
    with open('/home/alfaro/zavor_web/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Remove {% load static %}
    html = html.replace('{% load static %}', '')
    
    # 2. Replace static tags. {% static 'ruta' %} -> static/ruta
    import re
    # Match {% static 'ruta/archivo' %} or {% static "ruta/archivo" %}
    html = re.sub(r'\{%\s*static\s+[\'"](.*?)[\'"]\s*%\}', r'static/\1', html)
    
    # Also handle dynamic static tags: {% static place.image %} -> static/{{ place.image }}
    html = re.sub(r'\{%\s*static\s+([a-zA-Z0-9_.]+)\s*%\}', r'static/{{\1}}', html)
    
    # 3. Handle urls. {% url 'landing:download_apk' %} -> firebase url
    firebase_url = "https://firebasestorage.googleapis.com/v0/b/zavor-fe238.firebasestorage.app/o/app%2FZavoR.apk?alt=media&token=90d69524-8611-4a3b-af6b-e96f00d935e3"
    html = re.sub(r'\{%\s*url\s+[\'"]landing:download_apk[\'"]\s*%\}', firebase_url, html)
    
    # 4. Any other urls -> #
    html = re.sub(r'\{%\s*url\s+.*?%\}', '#', html)

    # Now render with django template engine
    from django.template import Template, Context
    t = Template(html)
    c = Context(context_dict)
    rendered_html = t.render(c)
    
    # Guardar en index.html
    with open('/home/alfaro/zavor_web/index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)
        
    print("Static rendering complete!")

if __name__ == '__main__':
    render_standalone()
