# Generated by Django 4.0.3 on 2022-03-19 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
