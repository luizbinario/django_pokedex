from django.contrib import admin

# Register your models here.

#BEGIN - Pokedex
from .models import Pokemon

def make_public(modeladmin, request, queryset):
    queryset.update(public=True)
make_public.short_description = "Make public selected pokemons"

def make_private(modeladmin, request, queryset):
    queryset.update(public=False)
make_private.short_description = "Make private selected pokemons"

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'pokemon', 'element', 'public')
    list_display_links = ('id', 'pokemon')
    ordering = ['id']
    actions = [make_public, make_private]

admin.site.register(Pokemon, PokemonAdmin)
#END - Pokedex
