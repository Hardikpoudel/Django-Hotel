# Generated by Django 3.1.4 on 2021-01-28 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='eventReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noOfGuest', models.IntegerField()),
                ('totalPrice', models.IntegerField()),
                ('purposeDescribe', models.CharField(max_length=500)),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('reservationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation')),
            ],
        ),
    ]