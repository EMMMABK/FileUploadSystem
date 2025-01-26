from django.shortcuts import render, HttpResponse
from .forms import MyFileUploadForm
from .models import file_upload
# Create your views here.

def index(request):
    if request.method == "POST":
        c_form = MyFileUploadForm(request.POST, request.FILES)

        if c_form.is_valid():
            name = c_form.cleaned_data['file_name']
            files = c_form.cleaned_data['files']
            file_upload(file_name=name, my_file = files).save()

            return HttpResponse('File successfully uploaded!')
        else:
            return HttpResponse("File didn't uploaded.")
    else:
        context = {
            'form': MyFileUploadForm()
        }
        return render(request, 'FileUploadSystemApp/index.html', context)


def show_data(request):
    all_data = file_upload.objects.all()

    context = {
        'data': all_data
    }

    return render(request, 'FileUploadSystemApp/list.html', context)