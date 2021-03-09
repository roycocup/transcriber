from django.shortcuts import *
from django.http import *

from hashlib import *
import datetime as dt

from logging import *

from django.contrib.auth.models import *
from .forms import UploadFileForm
from .models import *


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
    if created:
        ext.save()

    Uploads(filename=name, user=user).save()

    with open(f'uploads/{name}', 'wb+') as destination:
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
    rows = len(uploads)
    

    return HttpResponse(f'processing {rows} rows\n')