# Generated by Django 3.1.3 on 2020-11-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area', '0005_auto_20201116_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='link',
            field=models.CharField(max_length=200, null='True'),
        ),
    ]