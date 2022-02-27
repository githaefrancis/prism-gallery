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

def search(request):
  if 'category_name' in request.GET and request.GET["category_name"]:
    search_term=request.GET.get("category_name")
    
    search_results=Image.search_image(search_term)
    message=f"results for {search_term}"
    context={
      "message":message,
      "images":search_results
    }
    print(search_results)

    return render(request,'search.html',context)


  else:
    message="You haven't searched for any term"
    return render(request,'search.html',{"message":message})

 

