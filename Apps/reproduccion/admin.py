from django.contrib import admin
from .models import Cancion,Genero,Album,Disquera,Playlist,PlaylistCanciones,UsuariosCanciones
# Register your models here.
admin.site.register(Cancion)
admin.site.register(Genero)
admin.site.register(Album)
admin.site.register(Disquera)
admin.site.register(PlaylistCanciones)
admin.site.register(Playlist)
admin.site.register(UsuariosCanciones)
