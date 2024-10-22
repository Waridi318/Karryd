from django.db import models


class Transportation(models.Model):
    weight = models.FloatField()
    LOCATION_CHOICES = [
        ('CITY4', 'City 4'),
        ('CITY5', 'City 5'),
        ('CITY6', 'City 6'),
        ('CITY7', 'City 7'),
    ]
    current_location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        default='CITY4',
    )
    DESTINATION_CHOICES = [
        ('CITY1', 'City 1'),
        ('CITY2', 'City 2'),
        ('CITY3', 'City 3'),
        # Add more choices as needed
    ]
    destination = models.CharField(
        max_length=20,
        choices=DESTINATION_CHOICES,
        default='CITY1',
    )
