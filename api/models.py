from django.db import models


class BookStatus(models.TextChoices):
    ACTIVE = 1, 'Active'
    INACTIVE = 2, 'Inactive'
    ARCHIVED = 3, 'Archived'
class TagStatus(models.TextChoices):
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

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField('Tag', related_name='products')

