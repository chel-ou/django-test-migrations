import uuid

from django.db import models


def hash_generator():
    return str(uuid.uuid4())[:10]


class Entity(models.Model):
    hashid = models.CharField(
        unique=True, default=hash_generator, editable=False, max_length=24,
    )
    name = models.CharField(max_length=200, blank=False,)
    description = models.TextField(blank=True, null=True,)
    website = models.URLField(blank=True, null=True,)
    industry = models.CharField(max_length=200, blank=True, null=True,)

    def __str__(self):
        return self.name


class Participant(models.Model):
    hashid = models.CharField(
        unique=True, default=hash_generator, editable=False, max_length=24,
    )
    first_name = models.CharField(max_length=200, blank=False,)
    last_name = models.CharField(max_length=200, blank=False,)
    position = models.CharField(max_length=200, blank=False,)
    mobile_phone = models.CharField(max_length=200, blank=False,)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
