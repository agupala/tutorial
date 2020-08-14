from django.utils.text import slugify
from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name=" Nombre")
    description = models.TextField(verbose_name="Description")
    slug = models.SlugField(blank=True, default="", verbose_name="Slug")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])
    
