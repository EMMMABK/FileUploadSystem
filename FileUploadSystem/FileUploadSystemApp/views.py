from django.shortcuts import render, HttpResponse
from .forms import MyFileUploadForm
# Create your views here.

def index(request):
    context = {
        'form': MyFileUploadForm()
    }
    return render(request, 'FileUploadSystemApp/index.html', context)
