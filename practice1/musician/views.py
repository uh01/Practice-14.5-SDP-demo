# musician/views.py
from django.shortcuts import render, redirect
from . import forms
# from .models import Musician
# from .forms import MusicianForm

def musician_list(request):
    musician_form = forms.MusicianForm()
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('musician_list')
        else:
            musician_form = forms.MusicianForm()
    return render(request, 'musician/musician.html', {'form1': musician_form})
    # musician = Musician.objects.all()
    # print(musician)
    # return render(request, 'musician/musician.html', {'data1': musician})

