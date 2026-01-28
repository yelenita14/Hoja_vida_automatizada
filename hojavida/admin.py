from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import DatosPersonales, ExperienciaLaboral, CursosRealizados, Reconocimientos, ProductosAcademicos, ProductosLaborales, VentaGarage

# Ocultar información del framework
AdminSite.site_header = "Panel de Administración - Hoja de Vida"
AdminSite.site_title = "Administración"
admin.site.site_header = "Panel de Administración - Hoja de Vida"
admin.site.site_title = "Administración"

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'perfilactivo')
    fieldsets = (
        ('Perfil Activo', {
            'fields': ('perfilactivo',)
        }),
        ('Datos Personales', {
            'fields': ('nombres', 'apellidos', 'numerocedula', 'sexo', 'fechanacimiento', 'nacionalidad', 'lugarnacimiento', 'estadocivil')
        }),
        ('Profesional', {
            'fields': ('descripcionperfil', 'licenciaconducir')
        }),
        ('Contacto', {
            'fields': ('telefonoconvencional', 'telefonofijo', 'sitioweb')
        }),
        ('Dirección', {
            'fields': ('direcciondomiciliaria', 'direcciontrabajo')
        }),
        ('Foto de Perfil', {
            'fields': ('foto_perfil',)
        }),
        ('Visibilidad en Sitio Web', {
            'fields': ('mostrar_experiencia', 'mostrar_cursos', 'mostrar_reconocimientos', 'mostrar_productos_academicos', 'mostrar_productos_laborales', 'mostrar_venta_garage'),
            'description': 'Controla qué secciones aparecen en el sitio web público'
        }),
        ('Visibilidad en PDF Descargable', {
            'fields': ('imprimir_experiencia', 'imprimir_reconocimientos', 'imprimir_cursos', 'imprimir_productos_academicos', 'imprimir_productos_laborales', 'imprimir_venta_garage'),
            'description': 'Controla qué secciones aparecen cuando se descarga el PDF'
        }),
    )
    search_fields = ('nombres', 'apellidos')

@admin.register(CursosRealizados)
class CursosRealizadosAdmin(admin.ModelAdmin):
    list_display = ('nombrecurso', 'entidadpatrocinadora', 'fechainicio', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'fechainicio')
    search_fields = ('nombrecurso', 'entidadpatrocinadora')
    fieldsets = (
        ('Curso', {
            'fields': ('idperfilconqueestaactivo', 'nombrecurso', 'entidadpatrocinadora', 'fechainicio', 'fechafin', 'totalhoras', 'descripcioncurso')
        }),
        ('Contacto', {
            'fields': ('nombrecontactoauspicia', 'telefonocontactoauspicia', 'emailempresapatrocinadora')
        }),
        ('Certificado (Imagen o PDF)', {
            'fields': ('rutacertificado',)
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('cargodesempenado', 'nombrempresa', 'fechainiciogestion', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'fechainiciogestion')
    search_fields = ('cargodesempenado', 'nombrempresa')
    fieldsets = (
        ('Experiencia', {
            'fields': ('idperfilconqueestaactivo', 'cargodesempenado', 'nombrempresa', 'lugarempresa', 'fechainiciogestion', 'fechafingestion', 'descripcionfunciones')
        }),
        ('Contacto Empresarial', {
            'fields': ('nombrecontactoempresarial', 'telefonocontactoempresarial', 'emailempresa', 'sitiowebempresa')
        }),
        ('Certificado (Imagen o PDF)', {
            'fields': ('rutacertificado',)
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )

@admin.register(Reconocimientos)
class ReconocimientosAdmin(admin.ModelAdmin):
    list_display = ('tiporeconocimiento', 'entidadpatrocinadora', 'fechareconocimiento', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'tiporeconocimiento', 'fechareconocimiento')
    search_fields = ('tiporeconocimiento', 'entidadpatrocinadora')
    fieldsets = (
        ('Reconocimiento', {
            'fields': ('idperfilconqueestaactivo', 'tiporeconocimiento', 'entidadpatrocinadora', 'fechareconocimiento', 'descripcionreconocimiento')
        }),
        ('Contacto', {
            'fields': ('nombrecontactoauspicia', 'telefonocontactoauspicia')
        }),
        ('Certificado (Imagen o PDF)', {
            'fields': ('rutacertificado',)
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )

@admin.register(ProductosAcademicos)
class ProductosAcademicosAdmin(admin.ModelAdmin):
    list_display = ('nombrerecurso', 'clasificador', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'clasificador')
    search_fields = ('nombrerecurso', 'descripcion')
    fieldsets = (
        ('Producto Académico', {
            'fields': ('idperfilconqueestaactivo', 'nombrerecurso', 'clasificador', 'descripcion')
        }),
        ('Recursos', {
            'fields': ('archivo', 'link')
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )

@admin.register(ProductosLaborales)
class ProductosLaboralesAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto', 'fechaproducto', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'fechaproducto')
    search_fields = ('nombreproducto', 'descripcion')
    fieldsets = (
        ('Producto Laboral', {
            'fields': ('idperfilconqueestaactivo', 'nombreproducto', 'fechaproducto', 'descripcion')
        }),
        ('Recursos', {
            'fields': ('archivo', 'link')
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )

@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto', 'valordelbien', 'estadoproducto', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'estadoproducto', 'fecha_publicacion')
    search_fields = ('nombreproducto', 'descripcion')
    fieldsets = (
        ('Producto para Venta', {
            'fields': ('idperfilconqueestaactivo', 'nombreproducto', 'valordelbien', 'estadoproducto', 'descripcion')
        }),
        ('Imagen (Obligatoria)', {
            'fields': ('imagen_producto',),
            'description': 'La imagen es obligatoria para mostrar el producto'
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )
