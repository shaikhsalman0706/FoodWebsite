from django.db import models


class Food(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    video = models.URLField()

    def __str__(self):
        return self.summary
