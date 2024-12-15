from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    cover = models.ImageField(upload_to="profile_covers/", blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username


class Listing(models.Model):
    name = models.CharField(max_length=200)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    seller_url = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to="listing_pics/", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return (
            f"{self.name=}; {self.seller=}; {self.price=}"
            f"{self.seller_url=}; {self.description=};"
        )
