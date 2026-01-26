import os
import base64
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from .models import (
    DATOSPERSONALES, EXPERIENCIALABORAL, CURSOSREALIZADOS,
    RECONOCIMIENTOS, ProductosAcademicos, ProductosLaborales, Ventas
)

def descargar_cv_pdf(request):
    # Obtener datos del perfil activo
    datos = DATOSPERSONALES.objects.filter(perfilactivo=1).first()
    if not datos:
        return HttpResponse("No hay datos para descargar", status=400)

    experiencias = EXPERIENCIALABORAL.objects.filter(
        idperfilconqueestaactivo=datos.idperfil,
        activarparaqueseveaenfront=1
    )
    cursos = CURSOSREALIZADOS.objects.filter(
        idperfilconqueestaactivo=datos.idperfil,
        activarparaqueseveaenfront=1
    )
    reconocimientos = RECONOCIMIENTOS.objects.filter(
        idperfilconqueestaactivo=datos.idperfil,
        activarparaqueseveaenfront=1
    )
    productos_academicos = ProductosAcademicos.objects.filter(
        idperfilconqueestaactivo=datos.idperfil,
        activarparaqueseveaenfront=1
    )
    productos_laborales = ProductosLaborales.objects.filter(
        idperfilconqueestaactivo=datos.idperfil,
        activarparaqueseveaenfront=1
    )
    ventas = Ventas.objects.filter(
        idperfilconqueestaactivo=datos.idperfil,
        activarparaqueseveaenfront=1
    )

    # Foto del perfil en base64
    foto_base64 = None
    foto_mime_type = 'image/jpeg'
    if datos.foto and os.path.exists(datos.foto.path):
        foto_path = datos.foto.path
        extension = foto_path.lower().split('.')[-1]
        if extension == 'png':
            foto_mime_type = 'image/png'
        elif extension == 'gif':
            foto_mime_type = 'image/gif'
        elif extension in ['jpg', 'jpeg']:
            foto_mime_type = 'image/jpeg'
        with open(foto_path, 'rb') as f:
            foto_base64 = base64.b64encode(f.read()).decode()

    # Convertir certificados de cursos a base64
    for c in cursos:
        c.certificado_base64 = None
        c.certificado_mime_type = 'application/octet-stream'
        if c.archivo_certificado and os.path.exists(c.archivo_certificado.path):
            path = c.archivo_certificado.path
            ext = path.lower().split('.')[-1]
            with open(path, 'rb') as f:
                c.certificado_base64 = base64.b64encode(f.read()).decode()
            if ext == 'pdf':
                c.certificado_mime_type = 'application/pdf'
            elif ext in ['jpg', 'jpeg']:
                c.certificado_mime_type = 'image/jpeg'
            elif ext == 'png':
                c.certificado_mime_type = 'image/png'

    # Convertir certificados de reconocimientos a base64
    for r in reconocimientos:
        r.certificado_base64 = None
        r.certificado_mime_type = 'application/octet-stream'
        if r.archivo_certificado and os.path.exists(r.archivo_certificado.path):
            path = r.archivo_certificado.path
            ext = path.lower().split('.')[-1]
            with open(path, 'rb') as f:
                r.certificado_base64 = base64.b64encode(f.read()).decode()
            if ext == 'pdf':
                r.certificado_mime_type = 'application/pdf'
            elif ext in ['jpg', 'jpeg']:
                r.certificado_mime_type = 'image/jpeg'
            elif ext == 'png':
                r.certificado_mime_type = 'image/png'

    # Convertir imágenes de ventas a base64
    for v in ventas:
        v.imagen_base64 = None
        if v.imagen and os.path.exists(v.imagen.path):
            with open(v.imagen.path, 'rb') as f:
                v.imagen_base64 = base64.b64encode(f.read()).decode()

    # Contexto para renderizar el HTML
    context = {
        'datos': datos,
        'experiencias': experiencias,
        'cursos': cursos,
        'reconocimientos': reconocimientos,
        'productos_academicos': productos_academicos,
        'productos_laborales': productos_laborales,
        'ventas': ventas,
        'es_pdf': True,
        'foto_base64': foto_base64,
        'foto_mime_type': foto_mime_type,
    }

    # Renderizar HTML
    html_string = render_to_string('hojavida/mi_hoja_vida_pdf.html', context)

    try:
        # Generar PDF con WeasyPrint
        html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
        pdf = html.write_pdf(stylesheets=[CSS(string='@page { size: A4; margin: 1cm }')])

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Hoja_de_Vida.pdf"'
        return response

    except Exception as e:
        print(f"✗ Error generando PDF con WeasyPrint: {e}")
        return HttpResponse(f"Error al generar PDF: {str(e)}", status=500)
