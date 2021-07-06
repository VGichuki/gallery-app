from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Location,Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    #view function that renders the home page
    images = Image.objects.all()
    return render(request, 'welcome.html', {"images": images})

# def search_results(request):
#   if 'art' in request.GET and request.GET["art"]:
#     search_term=request.GET.get('art')
#     searched_category=Category.search_category(search_term)    
#     results=Image.search_image(searched_category)
#     if results:
#       message=f"{search_term}"  
#       title='Results'

#       return render(request,'search.html',{"message":message,"images":results,"title":title})

#     else:
#       message="You haven't search for a category"  
#       title='Results'
#       return render(request, 'search.html',{"message":message,"title":title})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_articles})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

def images_by_location(request, location_name):
  try:
    found_location = Location.get_location(location_name)
    images = Image.get_images_by_location(found_location)
    title = location_name

  except ObjectDoesNotExist:
    raise Http404()

  return render(request, 'images.html', {"images":images , "title": title})

def images_by_category(request, category_name):
  try:
    found_category = Category.search_category(category_name)
    images = Image.search_image(found_category)
    title = category_name

  except ObjectDoesNotExist:
    raise Http404()

  return render(request, 'category.html',{"images":images, "title":title})

