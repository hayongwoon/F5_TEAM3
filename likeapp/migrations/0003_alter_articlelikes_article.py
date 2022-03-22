# Generated by Django 4.0.3 on 2022-03-21 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articleapp", "0001_initial"),
        ("likeapp", "0002_datcle_alter_articlelikes_article_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlelikes",
            name="article",
            field=models.ForeignKey(
                db_column="article",
                on_delete=django.db.models.deletion.CASCADE,
                to="articleapp.article",
            ),
        ),
    ]
