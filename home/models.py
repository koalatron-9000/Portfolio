from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Create your models here.
class Technology(models.Model):
    title = models.CharField(
            max_length=50,
            validators=[MinLengthValidator(3, "Title must be greater than 3 characters")]
    )    
    icon = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.title


class PortfolioItem(models.Model):
    title = models.CharField(
            max_length=100,
            validators=[MinLengthValidator(4, "Title must be greater than 4 characters")]
    )
    description = models.TextField()
    demonstration = models.ImageField(upload_to='uploads/')
    display = models.BooleanField()
    technologies = models.ManyToManyField(Technology)
    blurb = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
