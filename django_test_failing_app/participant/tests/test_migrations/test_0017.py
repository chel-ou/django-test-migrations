from django.core.management import call_command

from django_test_migrations.contrib.unittest_case import MigratorTestCase


class ParticipantMigration0017Test(MigratorTestCase):

    migrate_from = ('participant', '0010_remove_participant_hashid')
    migrate_to = ('participant', '0017_participant_populate_hashid')

    def prepare(self):
        participant_model = self.old_state.apps.get_model(
            'participant', 'Participant'
        )
        entity_model = self.old_state.apps.get_model('participant', 'Entity')

        entity = entity_model.objects.create(name='Entity')
        participant_model.objects.create(
            entity=entity,
            first_name='John',
            last_name='Doe',
            position='CEO',
            mobile_phone='1234',
        )
        participant_model.objects.create(
            entity=entity,
            first_name='John',
            last_name='Doe',
            position='CEO',
            mobile_phone='1234',
        )

    def test_migration_00017(self):
        participant_model = self.new_state.apps.get_model(
            'participant', 'Participant'
        )
        participant1 = participant_model.objects.first()
        participant2 = participant_model.objects.last()

        self.assertNotEqual(participant1.hashid, participant2.hashid)
        self.assertRegex(participant1.hashid, r'[0-9a-zA-Z]+')

    def tearDown(self):
        # call_command('migrate', verbosity=0)
        pass
