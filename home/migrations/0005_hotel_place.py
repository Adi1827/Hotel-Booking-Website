# Generated by Django 4.2.4 on 2023-09-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_hotel_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='place',
            field=models.CharField(default='place', max_length=100),
        ),
    ]