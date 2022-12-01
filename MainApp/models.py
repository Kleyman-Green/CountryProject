from django.db import models

class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=False)
    languages = models.TextField(blank=False)

    def __str__(self):
        return self.name