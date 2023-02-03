# Generated by Django 4.1.5 on 2023-02-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="backpull",
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
                ("date6", models.CharField(default="sideshoulder", max_length=100)),
                ("weight6", models.IntegerField(default=120)),
            ],
            options={
                "verbose_name_plural": "backpull Data",
            },
        ),
        migrations.CreateModel(
            name="CountryData",
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
                ("date", models.CharField(max_length=100)),
                ("weight", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "Country Pouplation Data",
            },
        ),
        migrations.CreateModel(
            name="deadlifting",
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
                ("date2", models.CharField(default="deadlifting", max_length=100)),
                ("weight2", models.IntegerField(default=120)),
            ],
            options={
                "verbose_name_plural": "new Pouplation Data",
            },
        ),
        migrations.CreateModel(
            name="frontshoulder",
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
                ("date4", models.CharField(default="sideshoulder", max_length=100)),
                ("weight4", models.IntegerField(default=120)),
            ],
            options={
                "verbose_name_plural": "Frontshoulder Data",
            },
        ),
        migrations.CreateModel(
            name="pullups",
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
                ("date7", models.CharField(default="sideshoulder", max_length=100)),
                ("weight7", models.IntegerField(default=120)),
            ],
            options={
                "verbose_name_plural": "pullups Data",
            },
        ),
        migrations.CreateModel(
            name="sideshoulder",
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
                ("date3", models.CharField(default="sideshoulder", max_length=100)),
                ("weight3", models.IntegerField(default=120)),
            ],
            options={
                "verbose_name_plural": "hi Pouplation Data",
            },
        ),
        migrations.CreateModel(
            name="squatting",
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
                ("date5", models.CharField(default="sideshoulder", max_length=100)),
                ("weight5", models.IntegerField(default=120)),
            ],
            options={
                "verbose_name_plural": "squatting Data",
            },
        ),
    ]
