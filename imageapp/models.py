from django.db import models

# Create your models here.

class add_image(models.Model):
    photo=models.ImageField()
    

    class Meta:
        verbose_name_plural ="image_upload"

    def __str__(self):
        return self.photo.name
