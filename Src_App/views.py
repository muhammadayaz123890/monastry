from django.shortcuts import render
from .models import *

def Index(request):


    return render(request, 'index.html')



def Home(request):

    context = {} 

    layout = Layout.objects.all()

    if layout:
    
        layout = layout[0]
        context['layout'] = layout
    
    return render(request, 'home.html', context)


def Brothers(request):

    context = {} 

    layout = Layout.objects.all()

    if layout:
    
        layout = layout[0]
        context['layout'] = layout

    return render(request, 'brothers.html', context)

def Gardens(request):

    return render(request, 'gardens.html')

def Retreat(request):

    context = {} 

    layout = Layout.objects.all()

    if layout:
    
        layout = layout[0]
        context['layout'] = layout

    return render(request, 'retreat.html')

def WeAre(request):

    return render(request, 'who-we-are.html')

def Grounds(request):

    return render(request, 'grounds-tour.html')

def DailyLife(request):


    return render(request, 'daily-life.html')

def Vacations(request):

    return render(request, 'vacations.html')

def PrayWithUs(request):

    return render(request, 'pray-with-us.html')

def Support(request):

    return render(request, 'support.html')

def LadyOfMepkin(request):
    context = {} 

    layout = Layout.objects.all()

    if layout:
    
        layout = layout[0]
        context['layout'] = layout
    return render(request, 'lady-of-mepkin.html', context)

def VirtualTour(request):

    return render(request, 'virtual-tour.html')

def LaurensCemetry(request):
    context = {} 

    layout = Layout.objects.all()

    if layout:
    
        layout = layout[0]
        context['layout'] = layout
    return render(request, 'laurens-cemetry.html', context)

def Artwork(request):

    artswork = Art_Work.objects.all()

    return render(request, 'artwork.html', {'art':artswork})