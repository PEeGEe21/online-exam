# Generated by Django 3.1.6 on 2021-05-06 13:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0023_exam_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
