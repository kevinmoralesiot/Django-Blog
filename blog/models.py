from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    portada = models.ImageField(upload_to='static/portadas/')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    categorias = models.ManyToManyField(Categoria)

    class Meta:
        verbose_name_plural = "Artículos"
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
