import csv
from django.db import models


class CargoModel(models.Model):
    # weight, description, zip_code_pick_up, zip_code_delivery будут обязательны к заполнению другие автоматом
    weight = models.PositiveSmallIntegerField()
    description = models.TextField()
    zip_code_pick_up = models.CharField(max_length=10, default=0)
    zip_code_delivery = models.CharField(max_length=10)

    city_pick_up = models.CharField(max_length=255, blank=True, null=True)
    state_pick_up = models.CharField(max_length=255, blank=True, null=True)
    lat_pick_up = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng_pick_up = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    pick_up = models.BooleanField(default=False)

    city_delivery = models.CharField(max_length=255, blank=True, null=True)
    state_delivery = models.CharField(max_length=255, blank=True, null=True)
    lat_delivery = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng_delivery = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    delivery = models.BooleanField(default=False)

    # Открываем uszips.csv находим совпадение по zip_code_pick_up
    def fill_location_data(self):
        with open('uszips.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['zip'] == self.zip_code_pick_up:
                    self.city_pick_up = row['city']
                    self.state_pick_up = row['state_name']
                    self.lat_pick_up = row['lat']
                    self.lng_pick_up = row['lng']
                    break

    # Открываем uszips.csv находим совпадение по zip_code_delivery
    def fill_location_delivery(self):
        with open('uszips.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['zip'] == self.zip_code_delivery:
                    self.city_delivery = row['city']
                    self.state_delivery = row['state_name']
                    self.lat_delivery = row['lat']
                    self.lng_delivery = row['lng']
                    break

    def save(self, *args, **kwargs):
        if not self.pick_up:
            self.fill_location_data()
            self.fill_location_delivery()
            self.pick_up = True
            self.delivery = True
        super().save(*args, **kwargs)