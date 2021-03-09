import os 
from django.shortcuts import *
from django.http import *
from hashlib import *
import datetime as dt
from libs.audioformatter import Audioformatter as af
from logging import *
from django.contrib.auth.models import *
from .forms import UploadFileForm
from .models import *

upload_folder = "uploads"

def index(request):
    if not _get_session(request):
        _set_session(request)
    session_value = _get_session(request)
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES, request)
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    
    return render(request, 'transcriber/home.html', {'form': form, 'session':session_value })
    

def handle_uploaded_file(_file, request):
    name = _file['file'].name
        
    user, created = User.objects.get_or_create(username='anonymous')
    if created:
        user.save()

    ext, created = User_Ext.objects.get_or_create(user=user, session=_get_session(request))
    if created: ext.save()
    
    uploads = Uploads(filename=name, user=user, hashed=_get_checksum(_file))
    uploads.save()

    with open(os.path.join([upload_folder, name]), 'wb+') as destination:
        for chunk in _file['file'].chunks():
            destination.write(chunk)

def _set_session(request):
    now = dt.datetime.now()
    now = bytes(str(now), encoding='utf-8')
    # if its not alredy set
    if not _get_session(request):
        request.session['user']  = md5(now).hexdigest()

def _get_session(request):
    return request.session.get('user', None)

def process(request):
    uploads = Uploads.objects.all()
    num_rows = len(uploads)
    
    for upload in uploads:
        file_name = os.path.join(upload_folder, upload.filename)
        size = os.path.getsize(file_name)
        ext = os.path.splitext(file_name)[1]
        
        # formater = af(file_name)
        # if ext != '.flac':
        #     formatter.format_to(file_name=file_name, file_type='flac')
        # if formatter.probe_channels()


        
    return HttpResponse(f'processing {num_rows} rows\n')

def _get_checksum(_file):
    file_name = _file['file'].name
    with open(file_name,"rb") as f:
        b_data = f.read() # read file as bytes
        return md5(b_data).hexdigest();
        