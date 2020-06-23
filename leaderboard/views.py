from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from django.contrib import messages
from .models import Leaderboard

from .fileProcessor import handle_uploaded_file

def viewAll(request):
    board=Leaderboard.objects.all()
    return render(request, 'leaderboard/sample.html', {'records': board})

def details(request, pk):
    detail=Leaderboard.objects.get(pk=pk)
    return render(request, 'leaderboard/detail.html',{ 'user': detail})

def updateBoard(request):
    form = UploadFileForm()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        response = handle_uploaded_file(request.FILES['file'])
        if response:
            return redirect('index')
        messages.info(request, 'Input file should be a CSV or JSON file.')
    else:
        form = UploadFileForm()
    return render(request, 'leaderboard/index.html', {'form': form})