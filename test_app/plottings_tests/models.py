from string import ascii_letters, digits
from random import choice
from django.db import models

chars = ascii_letters + digits


def generate_code(length=40):
    return ''.join([choice(chars) for _ in range(length)])


TYPE_CHOICES = [
        ("PNG", "PNG"),
        ("SVG", "SVG"),
        ]


class Plot(models.Model):
    code = models.CharField(max_length=100)
    plot = models.ImageField(upload_to="plots")
    _type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_code()
        super().save(*args, **kwargs)
