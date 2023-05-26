import csv
import random
import string
from django.db import models


def get_random_location():  # Рандомное заполнение локаций
    with open('uszips.csv') as f:
        reader = csv.DictReader(f)
        row = random.choice(list(reader))
        return {
            'zip': row['zip'],
            'city': row['city'],
            'state_name': row['state_name'],
            'lat': row['lat'],
            'lng': row['lng'],
        }


class TruckModel(models.Model):
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.random_sku()
        if not self.zip:
            location_data = get_random_location()
            self.zip = location_data['zip']
            self.city = location_data['city']
            self.state_name = location_data['state_name']
            self.lat = location_data['lat']
            self.lng = location_data['lng']

        super().save(*args, **kwargs)

    def random_sku(self):  # Уникальный номер
        num = random.randint(1000, 9999)
        letter = random.choice(string.ascii_uppercase)
        return f"{num}{letter}"

    # load_capacity обязателен к заполнению остальное заполниться автоматом
    load_capacity = models.PositiveSmallIntegerField()

    sku = models.CharField(max_length=5, unique=True, blank=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state_name = models.CharField(max_length=255, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return str(self.lat)
