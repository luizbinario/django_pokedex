# Generated by Django 3.1.2 on 2020-11-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_auto_20201106_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='element',
            field=models.CharField(choices=[('leaf', 'Leaf'), ('water', 'Water'), ('fire', 'Fire')], max_length=100),
        ),
    ]
