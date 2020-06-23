from django.db import models
from django.shortcuts import reverse

class Leaderboard(models.Model):

    fullname=models.CharField("fullname", max_length=50)
    email=models.EmailField("Email", max_length=254)
    username=models.CharField("Username", max_length=50)
    points=models.DecimalField("Points", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "leaderboard"
        verbose_name_plural = "leaderboards"
        ordering= ['points']

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("leader_detail", kwargs={"pk": self.pk})

