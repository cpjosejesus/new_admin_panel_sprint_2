# Generated by Django 4.2.5 on 2024-04-23 01:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.RunSQL(
                   sql="""
                       CREATE SCHEMA IF NOT EXISTS content;
                       """
               ),
        migrations.CreateModel(
            name="Filmwork",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                ("creation_date", models.DateTimeField(auto_now=True)),
                (
                    "file_path",
                    models.FileField(
                        blank=True, upload_to="film_works/", verbose_name="file_path"
                    ),
                ),
                (
                    "rating",
                    models.FloatField(
                        blank=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="rating",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("MV", "movie"), ("TV", "tv_show")], max_length=20
                    ),
                ),
            ],
            options={
                "verbose_name": "Filmwork",
                "verbose_name_plural": "Filmworks",
                "db_table": 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
            ],
            options={
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
                "db_table": 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=255, verbose_name="full_name"),
                ),
            ],
            options={
                "verbose_name": "Person",
                "verbose_name_plural": "Persons",
                "db_table": 'content"."person',
            },
        ),
        migrations.CreateModel(
            name="PersonFilmwork",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("role", models.TextField(verbose_name="role")),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "film_work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.person"
                    ),
                ),
            ],
            options={
                "db_table": 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name="GenreFilmwork",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "film_work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.genre"
                    ),
                ),
            ],
            options={
                "db_table": 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name="filmwork",
            name="genres",
            field=models.ManyToManyField(
                through="movies.GenreFilmwork", to="movies.genre"
            ),
        ),
        migrations.AddField(
            model_name="filmwork",
            name="persons",
            field=models.ManyToManyField(
                through="movies.PersonFilmwork",
                to="movies.person",
                verbose_name="persons",
            ),
        ),
        migrations.AddIndex(
            model_name="personfilmwork",
            index=models.Index(
                fields=["film_work_id", "person_id", "role"],
                name="film_work_person_idx",
            ),
        ),
        migrations.AddConstraint(
            model_name="personfilmwork",
            constraint=models.UniqueConstraint(
                fields=("film_work_id", "person_id", "role"),
                name="unique_film_work_person",
            ),
        ),
        migrations.AddIndex(
            model_name="genrefilmwork",
            index=models.Index(
                fields=["film_work_id", "genre_id"], name="film_work_genre_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="genrefilmwork",
            constraint=models.UniqueConstraint(
                fields=("film_work_id", "genre_id"), name="unique_film_work_genre"
            ),
        ),
    ]
