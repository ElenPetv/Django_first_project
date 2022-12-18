from django.db import models


# Create your models here.
class Library(models.Model):
    name = models.CharField('Book title', max_length=100)
    publishing = models.IntegerField('Publishing year')
    title = models.CharField('Author', max_length=100)

    def __str__(self):
        return f"book title - {self.name}, " \
               f"publishing year - {self.publishing}, author - {self.title}."
