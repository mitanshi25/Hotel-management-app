# Generated by Django 4.2.4 on 2023-09-22 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0002_rename_room_rooms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='room_category',
        ),
        migrations.AlterField(
            model_name='guest',
            name='room_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.rooms'),
        ),
    ]
