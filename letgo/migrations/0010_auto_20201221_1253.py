# Generated by Django 3.1.3 on 2020-12-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letgo', '0009_auto_20201221_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imggal',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='iconimage',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='mainimage',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
