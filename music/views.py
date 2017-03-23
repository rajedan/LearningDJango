from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album, Song
from django.http import Http404
# Create your views here.
# python functions goes here which takes request from user and give response in some kind of way


def index(request):
    all_albums = Album.objects.all();
    return render(request, 'music/index.html', {'all_albums' : all_albums})

""" primary way of rendering all db objects with template
def index(request):
    all_albums = Album.objects.all();
    template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums,
    }
    return HttpResponse(template.render(context, request))
"""
def detail(request, album_id):
    try:
        album = Album.objects.get(id = album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")

    return render(request, "music/detail.html", {'album':album})

def getAlbumFromDB(request, album):
    #logic goes here to get Album from DB
    pass