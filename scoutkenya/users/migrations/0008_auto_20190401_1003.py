# Generated by Django 2.1.7 on 2019-04-01 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190328_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='county',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='height',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='school',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='speed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sport',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='weight',
        ),
    ]
