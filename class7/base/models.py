from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # discount_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, default="456")
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
