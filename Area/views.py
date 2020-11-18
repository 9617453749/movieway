from django.shortcuts import render
from .models import *
# Create your views here.
def about(request):
    return render(request,'About.html')

def search(request):
    if request.method == 'GET':
        print('hello method')
        query = request.GET.get('q')
        print(query)
        movie = movies.objects.filter(Name__icontains=query)
        return render(request,'search.html',{'mvs':movie})
    else:
        print('Not good yet')
        return render(request,'search.html')

def info(request,id):
    obj = movies.objects.get(id=id)
    return render(request,'Details.html',{'obj':obj})

def index(request):
    mvs = movies.objects.all()
    return render(request,'index.html',{'mvs':mvs})