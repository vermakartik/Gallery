from django.db import models
import datetime
from . import utils

# Create your models here.
def calculate_reduction_factor(width):
    return (width / 512)

class Gallery(models.Model):
    title_text = models.CharField(max_length = 100)
    image_file = models.ImageField(upload_to = 'documents/%Y/%m/%d/', blank=False, null=False)
    upload_time = models.DateField(auto_now = True)
    
    class Meta:
        unique_together = ("title_text", 'upload_time')
