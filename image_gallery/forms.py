from django.forms import ModelForm
from . import models 

class GalleryForm(ModelForm):
    class Meta:
        model = models.Gallery
        fields = '__all__'

    def clean_title_text(self):
        title = self.cleaned_data['title_text']
        print("Got-title -> ", title)
        title = "-".join(title.split(" "))
        return title

