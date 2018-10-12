from django.db import models

# Create your models here.
#always run "python manage.py makemigrations" and "python manage.py migrations"
class Product(models.Model):
    title = models.CharField(max_length=120) #when using CharField max_length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='This is so cool')
    featured = models.BooleanField(default=False) #null = True, default = True
