from django.db import migrations, models

import participant.models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0017_participant_populate_hashid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='hashid',
            field=models.CharField(
                default=participant.models.hash_generator,
                editable=False,
                max_length=24,
                unique=True,
            ),
        ),
    ]
