# Generated by Django 3.1.3 on 2020-11-16 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area', '0003_remove_movies_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='Image',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
