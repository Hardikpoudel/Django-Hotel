from django.db import models

# Create your models here.


class picture(models.Model):
    photo = models.ImageField(upload_to='')
