from django.contrib import admin
from .models import Musician, Album

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'instrument_type')
    search_fields = ('first_name', 'last_name', 'instrument_type')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'musician', 'release_date', 'rating')
    list_filter = ('release_date', 'rating')
    search_fields = ('album_name', 'musician__first_name', 'musician__last_name')
