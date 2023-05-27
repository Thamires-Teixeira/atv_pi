from django.contrib import admin
from .models import Cliente, Locacao, Filme, Categoria
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome', 'email')

@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display=('nome', 'data')

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display=('titulo', 'valor', 'categoria')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome',)