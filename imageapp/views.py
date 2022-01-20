from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.

def index(request):
    return render(request,'index.html')
def insert_image(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        item=add_image(photo=file_url)
        item.save()
        return render(request,'index.html')