# Generated by Django 3.1.3 on 2020-11-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area', '0004_movies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Image',
            field=models.ImageField(upload_to='media/pics'),
        ),
    ]
