from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.




class TimeSheet(models.Model):
    date = models.DateField(auto_now=False,blank=True)
    time = models.PositiveIntegerField(blank=True,validators=[MinValueValidator(0), MaxValueValidator(24)])
    attachment = models.FileField(upload_to='media/attachment/')
    