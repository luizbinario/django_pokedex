from django.shortcuts import render
from django.http import HttpResponse

#Importando models
from .models import Pokemon

# Create your views here.
def home(request):
    return render(request, "index.html", {})

def pokedex_index(request):
    pokemons = Pokemon.objects.all()
    context = {'pokemons': pokemons}
    return render(request, "pokedex/index.html", context)

def handler404(request, *args, **kwargs):
    return render(request, '404.html', status=404)
