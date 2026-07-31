import os
import django
from django.test import Client

# Configurar Django para ejecutarse de forma independiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zavor_web.settings')
django.setup()

def export_homepage():
    client = Client()
    response = client.get('/')
    
    if response.status_code == 200:
        html = response.content.decode('utf-8')
        
        # 1. Reemplazar rutas estáticas (asumiendo que {% static ... %} renderizó algo como "/static/...")
        # Buscamos 'href="/static/' y 'src="/static/'
        html = html.replace('href="/static/', 'href="static/')
        html = html.replace('src="/static/', 'src="static/')
        
        # 2. Reemplazar enlaces a la vista de descarga si los hay, aunque el html ya renderizado tendrá href="/descargar/"
        # O podemos buscar "href=\"/descargar/\"" y reemplazar con la URL de Firebase
        firebase_url = "https://firebasestorage.googleapis.com/v0/b/zavor-fe238.firebasestorage.app/o/app%2FZavoR.apk?alt=media&token=90d69524-8611-4a3b-af6b-e96f00d935e3"
        html = html.replace('href="/descargar/"', f'href="{firebase_url}"')
        html = html.replace("href='/descargar/'", f"href='{firebase_url}'")
        
        # Eliminar posible barra diagonal base estatica o rutas sin el /static/ si las hubiera, pero Django por defecto pone /static/
        
        # Guardar en index.html de la raiz
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Export successful!")
    else:
        print(f"Error rendering homepage, status: {response.status_code}")

if __name__ == '__main__':
    export_homepage()
