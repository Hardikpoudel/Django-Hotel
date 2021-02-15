# Generated by Django 3.1.4 on 2021-02-10 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reserved'),
        ('room', '0003_room_roomslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomreservation',
            name='reservedID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='reservation.reserved'),
            preserve_default=False,
        ),
    ]