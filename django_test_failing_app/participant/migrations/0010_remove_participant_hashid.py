from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0002_auto_20190913_1235'),
    ]

    operations = [
        migrations.RemoveField(model_name='participant', name='hashid',),
    ]
