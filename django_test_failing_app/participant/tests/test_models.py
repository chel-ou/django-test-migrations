from django.core.exceptions import ValidationError
from django.test import TestCase

from participant.tests.factories import (
    EntityFactory,
    ParticipantFactory,
)


class EntityModelTest(TestCase):
    def test_name_cannot_be_blank(self):
        with self.assertRaises(ValidationError):
            EntityFactory(name='').full_clean()

    def test_entity_object_string(self):
        entity = EntityFactory(name='my entity')
        self.assertEqual(str(entity), 'my entity')


class ParticipantModelTest(TestCase):
    def test_first_name_cannot_be_blank(self):
        with self.assertRaises(ValidationError):
            ParticipantFactory(first_name='').full_clean()

    def test_last_name_cannot_be_blank(self):
        with self.assertRaises(ValidationError):
            ParticipantFactory(last_name='').full_clean()

    def test_position_cannot_be_blank(self):
        with self.assertRaises(ValidationError):
            ParticipantFactory(position='').full_clean()

    def test_mobile_phone_cannot_be_blank(self):
        with self.assertRaises(ValidationError):
            ParticipantFactory(mobile_phone='').full_clean()

    def test_entity_cannot_be_blank(self):
        participant = ParticipantFactory.build(entity=None)
        with self.assertRaises(ValidationError):
            participant.full_clean()
