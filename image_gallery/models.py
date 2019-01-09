from django.db import models
import datetime
# Create your models here.
class Gallery(models.Model):
    title_text = models.CharField(max_length = 100)
    image_file = models.FileField(upload_to = 'documents/%Y/%m/%d/', blank=False, null=False)
    upload_time = models.DateField(auto_now = True)
    
    class Meta:
        unique_together = ("title_text", 'upload_time')