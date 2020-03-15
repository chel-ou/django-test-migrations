import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='entity',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='participant.Entity',
            ),
        ),
    ]
