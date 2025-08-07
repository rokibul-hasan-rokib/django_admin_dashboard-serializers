from django.db import models


class BookStatus(models.TextChoices):
    ACTIVE = 1, 'Active'
    INACTIVE = 2, 'Inactive'
    ARCHIVED = 3, 'Archived'
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    status = models.IntegerField(
        choices=BookStatus.choices,
        default=BookStatus.ACTIVE
    )

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)