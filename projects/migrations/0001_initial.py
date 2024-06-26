# Generated by Django 5.0.6 on 2024-06-19 04:22

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('description', tinymce.models.HTMLField(blank=True, verbose_name='Aprašymas')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Nuotrauka')),
            ],
            options={
                'verbose_name': 'Kategorija',
                'verbose_name_plural': 'Kategorijos',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('description', tinymce.models.HTMLField(blank=True, verbose_name='Aprašymas')),
                ('technology', models.CharField(blank=True, max_length=50, verbose_name='Technologija')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Nuotrauka')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.category', verbose_name='Kategorija')),
            ],
            options={
                'verbose_name': 'Projektas',
                'verbose_name_plural': 'Projektai',
                'ordering': ['title'],
            },
        ),
    ]
