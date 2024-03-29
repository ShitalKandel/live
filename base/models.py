from django.db import models

import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True