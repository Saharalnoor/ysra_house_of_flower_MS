from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def faqs(request):
    """A view to return the faqs page"""

    return render(request, 'home/faqs.html')


def contact_us(request):
    """A view to return the contact_us page"""

    return render(request, 'home/contact_us.html')
