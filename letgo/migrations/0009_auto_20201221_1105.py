# Generated by Django 3.1.3 on 2020-12-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letgo', '0008_auto_20201221_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imggal',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
