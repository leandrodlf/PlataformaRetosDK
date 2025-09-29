from django.contrib import admin
from .models import Categoria, Reto, Alternativa, IntentoReto, PerfilUsuario

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 4

@admin.register(Reto)
class RetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'dificultad', 'tipo', 'categoria', 'puntos', 'activo']
    list_filter = ['dificultad', 'tipo', 'categoria', 'activo']
    search_fields = ['titulo', 'descripcion']
    inlines = [AlternativaInline]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']

@admin.register(IntentoReto)
class IntentoRetoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'reto', 'es_correcto', 'fecha_intento']
    list_filter = ['es_correcto', 'fecha_intento']

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'puntos_totales', 'retos_resueltos']

admin.site.register(Alternativa)