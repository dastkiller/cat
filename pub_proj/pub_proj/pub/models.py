import uuid

from django.db import models

# Create your models here.


class BookedModel(models.Model):
    booked_date = models.DateTimeField()
    booked_uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    table_id = models.IntegerField()
    person_count = models.IntegerField()


class TableModel(models.Model):
    id = models.IntegerField(primary_key=True)
    max_person_count = models.IntegerField(null=False)
