from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from .models import Wallpaper, Tags
from django.template import loader
from django.conf import settings
import mimetypes
import requests
import os
def index(request):
    walls_list = Wallpaper.objects.order_by("-pub_date")
    tags_list = Tags.objects.all()
    template = loader.get_template("walls/index.html")
    context = {'walls_list': walls_list, 'tags_list': tags_list}
    return HttpResponse(template.render(context, request))


def detail(request, wallpaper_id):
    wallpaper = Wallpaper.objects.get(id=wallpaper_id)
    tags = Tags.objects.all()
    template = loader.get_template("walls/detail.html")
    context = {'wall': wallpaper, 'tags_list': tags}
    return HttpResponse(template.render(context, request))


def download(request, wallpaper_id):
    wallpaper = Wallpaper.objects.get(id=wallpaper_id)
    file_path = wallpaper.image.path
    filename = os.path.basename(wallpaper.image.name)
    print(file_path)
    print(filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
    else:
        raise Http404
    
def sort(request, tag_id):
    tag = Tags.objects.get(id=tag_id)
    tags = Tags.objects.all()
    wallpapers = tag.wallpaper_set.all()
    template = loader.get_template("walls/index.html")
    context = {'walls_list': wallpapers, 'tags_list': tags}
    return HttpResponse(template.render(context, request))    