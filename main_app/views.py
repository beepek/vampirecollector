from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Bat, Victim
# Create your views here.
from django.http import HttpResponse
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bats_index(request):
    bats = Bat.objects.all()
    return render(request, 'bats/index.html', {'bats': bats})

def bats_detail(request, bat_id):
    bat = Bat.objects.get(id=bat_id)
    
    # we want to find the toys that don't belong to the cat!
    # id__in syntax is what call field lookups, get, exclude, or filter
    victims_bat_doesnt_have = Victim.objects.exclude(id__in = bat.victims.all().values_list('id'))

    # instatiate the form, to be rendered in the template
    feeding_form = FeedingForm() 


    return render(request, 'bats/detail.html', {'bat': bat, 'feeding_form': feeding_form, 'victims': victims_bat_doesnt_have})

def assoc_victim(request, bat_id, victim_id):
    bat = Bat.objects.get(id=bat_id)
    bat.victims.add(victim_id)
    return redirect('detail', bat_id=bat_id)


class BatCreate(CreateView):
    model = Bat     
    fields = ['name', 'description', 'breed', 'age']

class BatUpdate(UpdateView):
    model = Bat
    fields = ['name', 'description', 'breed', 'age']

class BatDelete(DeleteView):
    model = Bat
    success_url = '/bats/'         

def add_feeding(request, bat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bat_id = bat_id
        new_feeding.save()
    return redirect('detail', bat_id=bat_id)    

class VictimList(ListView):
    model = Victim

class VictimDetail(DetailView):
    model = Victim

class VictimCreate(CreateView):
    model = Victim
    fields = '__all__'

class VictimUpdate(UpdateView):
    model = Victim
    fields = ['name', 'age']

class VictimDelete(DeleteView):
    model = Victim
    success_url = '/victims/'     
