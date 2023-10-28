from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    photos = models.ForeignKey('Image', on_delete=models.CASCADE)
    release_date = models.DateField()
    mileage = models.IntegerField()
    engine_number = models.CharField(max_length=100)
    fuel = models.ForeignKey('Fuel', on_delete=models.CASCADE)
    transmission_type = models.ForeignKey('Transmission', on_delete=models.CASCADE)
    drive_type = models.ForeignKey('Drive', on_delete=models.CASCADE)
    configuration = models.ForeignKey('Configuration', on_delete=models.CASCADE)
    advertisement_link = models.URLField()

    def __str__(self):
        return f"{self.brand} {self.model}"


class Transmission(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Drive(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Configuration(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    link = models.CharField(max_length=1000)


class Fuel(models.Model):
    type = models.CharField(max_length=20)
