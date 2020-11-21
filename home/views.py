from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def faqs(request):
    """A view to return the faqs page"""

    return render(request, 'home/faqs.html')