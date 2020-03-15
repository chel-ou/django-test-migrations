from django.test import TestCase

from participant.tests.factories import (
    EntityFactory,
    ParticipantFactory,
)


class EntityFactoryTest(TestCase):
    def test_full_clean(self):
        EntityFactory().full_clean()


class ParticipantFactoryTest(TestCase):
    def test_full_clean(self):
        ParticipantFactory().full_clean()
