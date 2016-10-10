from django.db import models
from django.utils import timezone

class Currency(models.Model):
    name = models.CharField(max_length=75)
    short = models.CharField(max_length=75)
    note1 = models.CharField(max_length=100, blank=True)
    note2 = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return '%s' % (self.name)



class Partner(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date_sign_up = models.DateField(blank=False, default=timezone.now)
    currency = models.ForeignKey(Currency)
    note1 = models.CharField(max_length=100, blank=True)
    note2 = models.CharField(max_length=100, blank=True)
    note3 = models.TextField(blank=True)
    def __str__(self):
        return self.name
