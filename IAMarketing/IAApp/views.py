from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import os
from django.contrib.auth.decorators import login_required
from ArtificialIntelligence import algoritmoEjemplo as IAEj
from .forms import CSVFileForm

# Create your views here.

def iaHomeView (request):
    return render(request, "iaHome.html")

@login_required
def aboutUsView(request):
    return render(request, "aboutUs.html")

@login_required
def projectView(request):
    IAEj.createGraphic()
    return render(request, "Project.html")

def exampleView(request):
    corrMatrix = IAEj.createCorrMatrix()
    context = {
        'corrMatrix' : corrMatrix
    }
    return render(request, "IAExample.html", context)

@login_required
def projectFirstStep(request):
    form = CSVFileForm(request.POST, request.FILES)
    handle_uploaded_file(request.FILES['file'])
    return render(request, 'ProjectFirstStep.html', {'form': form})


def handle_uploaded_file(f):
    with open('IAApp/static/uploadedFile.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



