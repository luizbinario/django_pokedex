from django.contrib import admin

#Importando models
from .models import Pokemon

# Register your models here.

def make_public(modeladmin, request, queryset):
    queryset.update(public=True)
make_public.short_description = "Make public the selected pokemons"

def make_private(modeladmin, request, queryset):
    queryset.update(public=False)
make_private.short_description = "Make private the selected pokemons"

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'pokemon', 'element', 'public')
    list_display_links = ('id', 'pokemon')
    ordering = ['id']
    actions = [make_public, make_private]

admin.site.register(Pokemon, PokemonAdmin)
