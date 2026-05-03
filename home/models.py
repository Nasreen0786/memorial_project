from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    description = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='img/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
