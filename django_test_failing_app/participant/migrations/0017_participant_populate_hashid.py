from django.db import migrations

import participant.models


def generate_hashid(apps, schema_director):
    participant_model = apps.get_model('participant', 'Participant')
    for row in participant_model.objects.all():
        row.hashid = participant.models.hash_generator()
        row.save(update_fields=['hashid'])


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0016_participant_add_hashid_field'),
    ]

    operations = [
        migrations.RunPython(
            generate_hashid, reverse_code=migrations.RunPython.noop
        ),
    ]
