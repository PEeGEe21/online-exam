# Generated by Django 3.1.6 on 2021-04-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_auto_20210415_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10, verbose_name='Gender'),
        ),
    ]
