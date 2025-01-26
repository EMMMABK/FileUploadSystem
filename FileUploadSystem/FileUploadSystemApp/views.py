from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.shortcuts import get_object_or_404
from .forms import MyFileUploadForm
from .models import file_upload
# Create your views here.

def index(request):
    if request.method == "POST":
        c_form = MyFileUploadForm(request.POST, request.FILES)

        if c_form.is_valid():
            name = c_form.cleaned_data['file_name']
            files = c_form.cleaned_data['files']
            file_upload(file_name=name, my_file=files).save()

            message = "File successfully uploaded!"
        else:
            message = "File didn't upload."

        return render(request, "FileUploadSystemApp/upload_status.html", {"message": message})

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


def download_file(request, file_id):
    file_instance = get_object_or_404(file_upload, id=file_id)
    
    file_content = file_instance.my_file.read()  

    response = FileResponse(file_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_instance.file_name}"'
    
    return response