from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from django.contrib import messages

from .fileProcessor import handle_uploaded_file

def index(request):
    form = UploadFileForm()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        response = handle_uploaded_file(request.FILES['file'])
        if response:
            return render(request, 'leaderboard/sample.html', {'records': response['scores']})
        messages.info(request, 'Input file should be a CSV or JSON file.')
    else:
        form = UploadFileForm()
    return render(request, 'leaderboard/index.html', {'form': form})
