from django.db import migrations, models

import participant.models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0010_remove_participant_hashid'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='hashid',
            field=models.CharField(
                default=participant.models.hash_generator,
                editable=False,
                max_length=24,
                null=True,
            ),
        ),
    ]
