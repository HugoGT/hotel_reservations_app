from django.shortcuts import render

# Create your views here.

def index(request):
    """
    The landing page
    """

    return render(request, 'reservations/index.html')