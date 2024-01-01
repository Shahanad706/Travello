# Generated by Django 4.2.7 on 2023-11-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('month', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='picture')),
                ('desc', models.TextField()),
            ],
        ),
    ]
