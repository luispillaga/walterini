from django.shortcuts import render
from .models import Slide


# Create your views here.
def home(request):
    sliders = Slide.objects.all()
    return render(request, "home/home.html", {'sliders': sliders})
