from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, Http404
from django.views.generic import DetailView, ListView
from django.utils.dateparse import parse_date

from . import models
from . import forms

# Create your views here.
def upload(request):
    if request.method == "POST":
        print(request.FILES['image_file'])
        if request.FILES['image_file']:
            image_form = forms.GalleryForm(request.POST, request.FILES)
            if image_form.is_valid():
                image_obj = image_form.save()
        return HttpResponseRedirect(reverse("gallery:image_details", args=(str(image_obj.upload_time), str(image_obj.title_text)))) 
    else:
        print("GET METHOD LOADING POST...")
        image_form = forms.GalleryForm(label_suffix="")
        print(image_form)
        return render(request, 'image_gallery/upload.html', {"image_form": image_form})

def upload_detail(request, date, filename):
    # django model get 
    if type(date) != str:
        date = parse_date(date)
    image_object = None
    try:
        image_object = models.Gallery.objects.get(upload_time = date, title_text = filename)
    except models.Gallery.DoesNotExist:
        return Http404("Not Found")
    return render(request, 'image_gallery/upload_detail.html', {"image_object": image_object})

class GalleryListView(ListView):
    model = models.Gallery