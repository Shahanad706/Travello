# Generated by Django 4.2.7 on 2023-11-25 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='desc',
            new_name='b_desc',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='img',
            new_name='b_img',
        ),
    ]
