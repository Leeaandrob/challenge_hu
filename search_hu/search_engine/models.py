from __future__ import unicode_literals

from django.db import models


class Establishment(models.Model):
    index = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0} - {1}".format(self.name, self.city)


class AvailabilityEstablishment(models.Model):
    date = models.DateField()
    available = models.BooleanField()
    establishment = models.ForeignKey('Establishment',
                                      related_name='establishment_available')

    def __unicode__(self):
        return "{0} - {1} - {2}".format(
            self.establishment.name, self.available,
            self.date.strftime("%d/%m/%Y")
        )
