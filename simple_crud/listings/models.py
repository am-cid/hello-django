from django.db import models


# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    seller_url = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return (
            f"{self.name=}; {self.seller=}; {self.price=}"
            f"{self.seller_url=}; {self.description=};"
        )
