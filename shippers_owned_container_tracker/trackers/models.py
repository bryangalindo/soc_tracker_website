from django.db import models

from core.models import TimeStampedModel
from operators.models import Operator


class Tracker(TimeStampedModel):
    id = models.BigIntegerField(primary_key=True, serialize=True, unique=True)
    uuid = models.UUIDField(unique=True)
    reference_number = models.TextField(max_length=11)
    container_number = models.TextField(max_length=11)
    # TODO: Fulfill choices parameter
    move_type = models.TextField()
    operator_id = models.ForeignKey(to=Operator, null=True, blank=True, on_delete=models.SET_NULL)
    return_date = models.DateField(null=True, blank=True)
