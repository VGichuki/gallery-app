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

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_title = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_title})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

def images_by_category(request, category_name):
  try:
    found_category = Category.search_category(category_name)
    images = Image.search_image(found_category)
    title = category_name

  except ObjectDoesNotExist:
    raise Http404()

  return render(request, 'category.html',{"images":images, "title":title})

def location(request):
    if 'location' in request.GET and request.GET["location"]:
        location = request.GET.get("location")
        searched_images = Image.filter_by_location(location)
        message = f"{location}"
        return render(request,"search.html",{"message":message,"images":searched_images})

    else:
        message = "select location to filter"
        return render(request,"search.html",{"message":message})

