import factory
from factory.django import DjangoModelFactory


class EntityFactory(DjangoModelFactory):
    class Meta:
        model = 'participant.Entity'
        django_get_or_create = ('name',)

    name = factory.Faker('company')


class ParticipantFactory(DjangoModelFactory):
    class Meta:
        model = 'participant.Participant'

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    position = factory.Faker('job')
    mobile_phone = factory.Faker('phone_number')
    entity = factory.SubFactory(EntityFactory)
