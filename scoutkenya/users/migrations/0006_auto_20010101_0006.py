# Generated by Django 2.1.7 on 2001-01-01 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190327_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='county',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(default='', max_length=100),
        ),
    ]