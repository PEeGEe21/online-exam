# Generated by Django 3.1.6 on 2021-03-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20210322_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='subject',
        ),
        migrations.AddField(
            model_name='exam',
            name='course',
            field=models.CharField(default='', max_length=20, verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='dept',
            field=models.CharField(choices=[('Maths_&_Comp', 'Maths and Computer Science'), ('BioChem', 'BioChemistry'), ('Accounting', 'Accounting'), ('Economics', 'Economics'), ('History', 'History'), ('Mass Commuication', 'Mass Commuication')], default=None, max_length=100, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Reg No.'),
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(default=None, max_length=20, verbose_name='Major'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='dept',
            field=models.CharField(choices=[('Maths_&_Comp', 'Maths and Computer Science'), ('BioChem', 'BioChemistry'), ('Accounting', 'Accounting'), ('Economics', 'Economics'), ('History', 'History'), ('Mass Commuication', 'Mass Commuication')], default=None, max_length=20, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default=None, max_length=254, verbose_name='Email'),
        ),
    ]