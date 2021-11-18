from django.contrib import admin

from core.models import Evento
# Register your models here.

#defino quais campos quero que aparece no painel admin
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo', 'data_evento')

admin.site.register(Evento, EventoAdmin)


