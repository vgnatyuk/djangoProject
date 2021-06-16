from django.db import models


# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=30)
    apartment_id = models.IntegerField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'apartment_id'], name='unique name-apartment')]


class AnotherModel(models.Model):
    another_name = models.CharField(max_length=30)
    another_id = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Another'
