# Generated by Django 4.0.3 on 2022-03-21 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("likeapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Datcle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="articlelikes",
            name="article",
            field=models.ForeignKey(
                db_column="article",
                on_delete=django.db.models.deletion.CASCADE,
                to="likeapp.datcle",
            ),
        ),
        migrations.AlterField(
            model_name="commentlikes",
            name="comment",
            field=models.ForeignKey(
                db_column="comment",
                on_delete=django.db.models.deletion.CASCADE,
                to="likeapp.datcle",
            ),
        ),
    ]
