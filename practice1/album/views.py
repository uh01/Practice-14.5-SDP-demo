# album/views.py
from django.shortcuts import render, redirect
from . import forms
# from .models import Album
# from .forms import AlbumForm

def album_list(request):
    album_form = forms.AlbumForm()
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('album_list')
        else:
            album_form = forms.AlbumForm()

    return render(request, 'album/album.html', {'form2': album_form})
    # album = Album.objects.all()
    # print(album)
    # return render(request, 'album/album.html', {'data2': album})
