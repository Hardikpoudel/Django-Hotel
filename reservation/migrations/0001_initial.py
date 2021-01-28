# Generated by Django 3.1.4 on 2021-01-28 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkIn', models.DateTimeField()),
                ('checkOut', models.DateTimeField()),
                ('tsCreated', models.DateTimeField(editable=False)),
                ('tsUpdated', models.DateTimeField()),
                ('guestID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.guest')),
            ],
        ),
    ]