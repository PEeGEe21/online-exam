# Generated by Django 3.1.6 on 2021-05-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0024_auto_20210506_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='image'),
        ),
    ]