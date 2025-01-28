from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='player_photos/')
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name