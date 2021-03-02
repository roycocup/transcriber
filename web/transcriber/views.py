from django.shortcuts import *
from django.http import *
from .forms import UploadFileForm


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES)
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    
    return render(request, 'transcriber/home.html', {'form': form})
    

def handle_uploaded_file(_file):
    name = _file['file'].name
    with open(f'uploads/{name}', 'wb+') as destination:
        for chunk in _file['file'].chunks():
            destination.write(chunk)
