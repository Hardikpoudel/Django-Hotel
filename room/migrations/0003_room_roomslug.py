# Generated by Django 3.1.4 on 2021-02-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_pictureid'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='roomSlug',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
