# Generated by Django 4.0.3 on 2022-04-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0006_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y%m%d'),
        ),
    ]
