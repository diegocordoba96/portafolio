# Generated by Django 4.2 on 2023-04-09 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='imagen',
            field=models.ImageField(upload_to='portafolio/imagenes/'),
        ),
    ]
