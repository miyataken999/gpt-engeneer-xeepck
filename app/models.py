from django.db import models

class Ring(models.Model):
    material = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    damage = models.TextField(blank=True)
    scratches = models.TextField(blank=True)

    def __str__(self):
        return f"Ring ({self.material}, {self.size}, {self.weight}g)"