from pathlib import Path
from django.db import models


class Plot(models.Model):
    plot = models.ImageField(upload_to="plots/")
