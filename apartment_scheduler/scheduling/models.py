from django.db import models
from django.contrib.postgres.fields import JSONField

class Zone(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Runner(models.Model):
    name = models.CharField(max_length=100)
    zones = models.ManyToManyField(Zone, related_name='runners')
    availability = models.JSONField()

    def __str__(self):
        return self.name

class Apartment(models.Model):
    address = models.CharField(max_length=255)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='apartments')
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE, related_name='apartments')
    availability = models.JSONField()  # Example: {"Monday": ["09:00", "09:15", ...], ...}

    def __str__(self):
        return self.address

class PotentialTenant(models.Model):
    name = models.CharField(max_length=100)
    offer = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Visit(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='visits')
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE, related_name='visits')
    tenants = models.ManyToManyField(PotentialTenant, related_name='visits')
    date = models.DateField()
    time_slot = models.TimeField()
    visit_order = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Visit to {self.apartment.address} on {self.date} at {self.time_slot}"
