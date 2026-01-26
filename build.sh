#!/usr/bin/env bash
set -o errexit

# SECCIÓN WKHTMLTOPDF 
# Crear carpeta para binarios si no existe
mkdir -p bin
# Descargar binario genérico si no existe (0.12.4 es el más estable para entornos sin dependencias)
if [ ! -f bin/wkhtmltopdf ]; then
  echo "Descargando wkhtmltopdf..."
  curl -L https://github.com -o wkhtml.tar.xz
  tar -xf wkhtml.tar.xz
  cp wkhtmltox/bin/wkhtmltopdf bin/
  rm -rf wkhtmltox wkhtml.tar.xz
fi

# Dar permisos al binario
chmod +x bin/wkhtmltopdf

# Instalar librerías Python
pip install -r requirements.txt

# Archivos estáticos
python manage.py collectstatic --no-input

# Migraciones
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py migrate

# Crear usuario admin 
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'Karen'
password = 'Karen1234'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email='', password=password)
    print(f'USUARIO {username} CREADO CON EXITO')
else:
    print(f'EL USUARIO {username} YA EXISTE EN POSTGRES')
END
