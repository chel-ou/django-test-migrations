import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0020_auto_20200116_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'participant',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='participant.Participant',
                    ),
                ),
            ],
        ),
    ]
