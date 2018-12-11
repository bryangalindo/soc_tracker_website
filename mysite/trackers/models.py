from django.db import models
from enum import Enum
import uuid


from core.models import TimeStampedModel
from vendors.models import Vendor
from depots.models import Depot


class Tracker(TimeStampedModel):
    class MOVETYPE(Enum):
        inland = ('inland', 'INLAND')
        port = ('port', 'PORT')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    last_free_day = models.DateField()
    reference_number = models.TextField(max_length=11)
    container_number = models.TextField(max_length=11)
    move_type = models.TextField(max_length=6, choices=[x.value for x in MOVETYPE])
    vendor = models.ForeignKey(to=Vendor, null=True, blank=True, on_delete=models.SET_NULL)
    depot = models.ForeignKey(to=Depot, null=True, blank=True, on_delete=models.SET_NULL)
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_free_day']

    def __str__(self):
        return self.container_number

