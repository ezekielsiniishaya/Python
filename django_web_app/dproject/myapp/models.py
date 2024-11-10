from django.db import models

class CustomUser(models.Model):
    name = models.CharField(max_length=15)
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    book = models.OneToOneField('Book', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='books', default='')
    publication_date = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.title} by {self.author}"

