from django.db import models

from core.models import TimeStampedModel


class Operator(TimeStampedModel):
    id = models.BigIntegerField(primary_key=True, serialize=True, unique=True)
    name = models.TextField(max_length=50)
    # TODO: Fulfill choices parameter
    type = models.TextField()
