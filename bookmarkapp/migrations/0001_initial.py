# Generated by Django 4.0.3 on 2022-03-18 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articleapp', '0002_article_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(db_column='article', on_delete=django.db.models.deletion.CASCADE, to='articleapp.article')),
            ],
            options={
                'db_table': 'user_bookmark',
            },
        ),
    ]
