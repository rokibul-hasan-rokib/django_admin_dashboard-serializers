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