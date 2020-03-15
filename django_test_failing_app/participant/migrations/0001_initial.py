import uuid

from django.db import migrations, models

import participant.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'hashid',
                    models.CharField(
                        default=participant.models.hash_generator,
                        editable=False,
                        max_length=24,
                        unique=True,
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=200, verbose_name='entity name',
                    ),
                ),
            ],
            options={'abstract': False,},
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'hashid',
                    models.CharField(
                        default=participant.models.hash_generator,
                        editable=False,
                        max_length=24,
                        unique=True,
                    ),
                ),
                (
                    'first_name',
                    models.CharField(
                        max_length=200, verbose_name='first name'
                    ),
                ),
                (
                    'last_name',
                    models.CharField(max_length=200, verbose_name='last name'),
                ),
                (
                    'position',
                    models.CharField(max_length=200, verbose_name='position'),
                ),
                (
                    'mobile_phone',
                    models.CharField(
                        max_length=200, verbose_name='mobile phone'
                    ),
                ),
            ],
            options={'abstract': False,},
        ),
    ]
