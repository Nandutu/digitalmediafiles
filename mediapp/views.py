from django.shortcuts import render
from .models import Photo, Video

# Create your views here.

def  photos(request):
	photos = Photo.objects.all()#.order_by('-id')
	return render(request, "mediapp/photos.html", {'photos':photos})

def  videos(request):
	videos = Video.objects.all()#.order_by('-id')	
	return render(request, "mediapp/videos.html", {'videos':videos})
