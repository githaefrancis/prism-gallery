from django.shortcuts import render
from .models import Image
# Create your views here.

def index(request):
  return render(request,'index.html')


def gallery(request):
  images=Image.get_all_images()
  context={
    'images':images,
  }
  print(images)
  return render(request,'gallery.html',context)