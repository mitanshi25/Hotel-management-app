# Generated by Django 4.2.4 on 2023-09-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0004_remove_guest_check_in_guest_check_in_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='id',
        ),
        migrations.AlterField(
            model_name='guest',
            name='gov_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
