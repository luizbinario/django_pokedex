from django.db import models

# Create your models here.
class Pokemon(models.Model):
    ELEMENTS = (('leaf', 'Leaf'), ('water', 'Water'), ('fire', 'Fire'))
    pokemon = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='static/images/pokemons/')
    element = models.CharField(max_length=100, blank=True, choices=ELEMENTS)
    public = models.BooleanField(default=False)
