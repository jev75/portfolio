from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Pavadinimas')
    description = HTMLField(blank=True, verbose_name='Aprašymas')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Nuotrauka')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategorija'
        verbose_name_plural = 'Kategorijos'
        ordering = ['title']

class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategorija')
    title = models.CharField(max_length=100, verbose_name='Pavadinimas')
    description = HTMLField(blank=True, verbose_name='Aprašymas')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Nuotrauka')

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100] if self.description else ''

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('projects:project_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Projektas'
        verbose_name_plural = 'Projektai'
        ordering = ['title']

class Review(models.Model):
    project = models.ForeignKey(Project, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Atsiliepimas')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Atsiliepimas'
        verbose_name_plural = 'Atsiliepimai'
        ordering = ['-created_at']

    def __str__(self):
        return f'Atsiliepimas {self.user.username} apie {self.project.title}'