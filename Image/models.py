from django.db import models

# Create your models here.


class picture(models.Model):
    photo1 = models.ImageField(upload_to='', null=True)
    photo2 = models.ImageField(upload_to='', null=True)
    photo3 = models.ImageField(upload_to='', null=True)
    photo4 = models.ImageField(upload_to='', null=True)
