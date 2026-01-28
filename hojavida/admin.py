from django.contrib import admin
from .models import DatosPersonales, ExperienciaLaboral, CursosRealizados, Reconocimientos, ProductosAcademicos, ProductosLaborales, VentaGarage

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'perfilactivo')
    fieldsets = (
        ('Perfil', {
            'fields': ('nombres', 'apellidos', 'descripcionperfil', 'perfilactivo')
        }),
        ('Datos Personales', {
            'fields': ('numerocedula', 'nacionalidad', 'lugarnacimiento', 'fechanacimiento', 'sexo', 'estadocivil', 'licenciaconducir')
        }),
        ('Contacto', {
            'fields': ('telefonoconvencional', 'telefonofijo', 'sitioweb')
        }),
        ('Dirección', {
            'fields': ('direcciondomiciliaria', 'direcciontrabajo')
        }),
        ('Foto', {
            'fields': ('foto_perfil',)
        }),
        ('Visibilidad en Web', {
            'fields': ('mostrar_experiencia', 'mostrar_cursos', 'mostrar_reconocimientos', 'mostrar_productos_academicos', 'mostrar_productos_laborales', 'mostrar_venta_garage')
        }),
        ('Visibilidad en PDF', {
            'fields': ('imprimir_experiencia', 'imprimir_reconocimientos', 'imprimir_cursos', 'imprimir_productos_academicos', 'imprimir_productos_laborales', 'imprimir_venta_garage')
        }),
    )

@admin.register(CursosRealizados)
class CursosRealizadosAdmin(admin.ModelAdmin):
    list_display = ('nombrecurso', 'idperfilconqueestaactivo', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'fechainicio')
    fieldsets = (
        ('Curso', {
            'fields': ('idperfilconqueestaactivo', 'nombrecurso', 'entidadpatrocinadora', 'fechainicio', 'fechafin', 'totalhoras', 'descripcioncurso')
        }),
        ('Contacto', {
            'fields': ('nombrecontactoauspicia', 'telefonocontactoauspicia', 'emailempresapatrocinadora')
        }),
        ('Certificado', {
            'fields': ('rutacertificado',)
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('cargodesempenado', 'nombrempresa', 'idperfilconqueestaactivo', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'fechainiciogestion')
    fieldsets = (
        ('Experiencia', {
            'fields': ('idperfilconqueestaactivo', 'cargodesempenado', 'nombrempresa', 'lugarempresa', 'fechainiciogestion', 'fechafingestion', 'descripcionfunciones')
        }),
        ('Contacto Empresarial', {
            'fields': ('nombrecontactoempresarial', 'telefonocontactoempresarial', 'emailempresa', 'sitiowebempresa')
        }),
        ('Certificado', {
            'fields': ('rutacertificado',)
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )

@admin.register(Reconocimientos)
class ReconocimientosAdmin(admin.ModelAdmin):
    list_display = ('tiporeconocimiento', 'idperfilconqueestaactivo', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'fechareconocimiento')
    fieldsets = (
        ('Reconocimiento', {
            'fields': ('idperfilconqueestaactivo', 'tiporeconocimiento', 'entidadpatrocinadora', 'fechareconocimiento', 'descripcionreconocimiento')
        }),
        ('Contacto', {
            'fields': ('nombrecontactoauspicia', 'telefonocontactoauspicia')
        }),
        ('Certificado', {
            'fields': ('rutacertificado',)
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )

@admin.register(ProductosAcademicos)
class ProductosAcademicosAdmin(admin.ModelAdmin):
    list_display = ('nombrerecurso', 'idperfilconqueestaactivo', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'clasificador')
    fieldsets = (
        ('Producto', {
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
    list_display = ('nombreproducto', 'idperfilconqueestaactivo', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'fechaproducto')
    fieldsets = (
        ('Producto', {
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
    list_display = ('nombreproducto', 'idperfilconqueestaactivo', 'valordelbien', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'estadoproducto', 'fecha_publicacion')
    fieldsets = (
        ('Producto', {
            'fields': ('idperfilconqueestaactivo', 'nombreproducto', 'estadoproducto', 'valordelbien', 'descripcion')
        }),
        ('Multimedia', {
            'fields': ('imagen_producto',)
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront',)
        }),
    )
