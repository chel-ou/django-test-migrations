from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0018_participant_hashid_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='description',
            field=models.TextField(
                blank=True, null=True, verbose_name='description'
            ),
        ),
        migrations.AddField(
            model_name='entity',
            name='industry',
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name='industry'
            ),
        ),
        migrations.AddField(
            model_name='entity',
            name='website',
            field=models.URLField(
                blank=True, null=True, verbose_name='website'
            ),
        ),
    ]
