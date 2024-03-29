from django.shortcuts import render
from .models import Image,Location
# Create your views here.
from django.http import Http404

def index(request):
  locations_list=Location.get_all_locations()
  context={
    'location_list':locations_list,
  }
  return render(request,'index.html',context)


def gallery(request):
  locations_list=Location.get_all_locations()
  
  images=Image.get_all_images()
  context={
    'images':images,
    'location_list':locations_list,

  }
  print(images)
  return render(request,'gallery.html',context)

def search(request):
  if 'category_name' in request.GET and request.GET["category_name"]:

    locations_list=Location.get_all_locations()
    
    try:

      search_term=request.GET.get("category_name")
      
      search_results=Image.search_image(search_term)
      message=f"results for {search_term}"
      context={
        "message":message,
        "images":search_results,
        "location_list":locations_list,
        

      }
      print(search_results)

      return render(request,'search.html',context)
    
    except ValueError:
      raise Http404()



  else:
    message="You haven't searched for any term"
    return render(request,'search.html',{"message":message})


def filter_by_location(request,location):
  '''
  Method to fetch
  '''
  locations_list=Location.get_all_locations()

  try:
    filter_results=Image.filter_by_location(location)
    context={
      "images":filter_results,
      "location":location,
      "location_list":locations_list,

    }

    return render(request,'location.html',context)

  except ValueError:
    raise Http404()
    
 

