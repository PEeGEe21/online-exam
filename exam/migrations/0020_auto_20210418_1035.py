# Generated by Django 3.1.6 on 2021-04-18 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0019_auto_20210418_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='passwor1',
            new_name='password1',
        ),
    ]
