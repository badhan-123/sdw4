from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

def musician_list(request):
    musicians = Musician.objects.all().prefetch_related('albums')
    return render(request, 'directory/musician_list.html', {'musicians': musicians})

def musician_create(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm()
    return render(request, 'directory/musician_form.html', {'form': form, 'title': 'Add Musician'})

def musician_edit(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'directory/musician_form.html', {'form': form, 'title': 'Edit Musician'})

def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm()
    return render(request, 'directory/album_form.html', {'form': form, 'title': 'Add Album'})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'directory/album_form.html', {'form': form, 'title': 'Edit Album'})

def musician_delete(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'POST':
        musician.delete()
        return redirect('musician_list')
    return render(request, 'directory/musician_confirm_delete.html', {'musician': musician})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('musician_list')
    return render(request, 'directory/album_confirm_delete.html', {'album': album})
