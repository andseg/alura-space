from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'legenda')
    list_display_links = ('id', 'nome', 'legenda')
    search_fields = ('nome', 'legenda', 'categoria')

admin.site.register(Fotografia, ListandoFotografias)



# Register your models here.
