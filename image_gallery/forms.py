from django.forms import ModelForm
from . import models 

class GalleryForm(ModelForm):
    class Meta:
        model = models.Gallery
        fields = '__all__'

