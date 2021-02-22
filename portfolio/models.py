from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha edición')

    class Meta:
        abstract = True

class Project(BaseModel):
    title = models.CharField(max_length = 100, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripcion')
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'projects')
    url = models.URLField(null=True, blank=True, verbose_name="Direccion web")

    class Meta():
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']
    
    def __str__(self):
        return self.title