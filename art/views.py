from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Location,Image

# Create your views here.
def welcome(request):
    #view function that renders the home page
    return render(request, 'welcome.html')

def search_results(request):
  if 'art' in request.GET and request.GET["art"]:
    search_term=request.GET.get('art')
    searched_category=Category.search_category(search_term)    
    results=Image.search_image(searched_category)
    if results:
      message=f"{search_term}"  
      title='Results'

      return render(request,'search.html',{"message":message,"images":results,"title":title})

    else:
      message="You haven't search for a category"  
      title='Results'
      return render(request, 'search.html',{"message":message,"title":title})

