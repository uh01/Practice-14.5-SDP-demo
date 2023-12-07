from django.shortcuts import render
from album.models import Album
from musician.models import Musician


def base(request):
    return render(request, 'base.html')

def home(request):
    albums = Album.objects.all()
    musicians = Musician.objects.all()

    return render(request, 'home.html', {'albums': albums, 'musicians': musicians})