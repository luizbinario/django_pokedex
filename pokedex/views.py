from django.shortcuts import render
from django.http import HttpResponse

#Importando models
from .models import Pokemon

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def pokedex(request):
    pokemons = Pokemon.objects.all()
    context = {'pokemons': pokemons}
    return render(request, "pokedex/index.html", context)
