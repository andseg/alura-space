from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'legenda', 'publicada', 'data_fotografia')
    list_display_links = ('id', 'nome', 'legenda')
    search_fields = ('nome', 'legenda', 'categoria')
    list_filter = ('categoria',)
    list_editable = ('publicada', 'data_fotografia')
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)



# Register your models here.
