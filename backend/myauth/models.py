from django.db import models
from eav.decorators import register_eav

# Create your models here.
@register_eav()
class TestModel(models.Model):
    label = models.CharField(max_length=50)