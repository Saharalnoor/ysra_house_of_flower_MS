from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """A view to return the about page"""

    return render(request, 'home/about.html')


def faqs(request):
    """A view to return the faqs page"""

    return render(request, 'home/faqs.html')


def contact_us(request):
    """A view to return the contact_us page"""
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.info(request, 'Your contactform has been submitted.\
                I will respond to you as soon as possible!')
            return redirect(reverse('contact'))
    else:
        f = ContactForm()
    return render(request, 'home/contact_us.html', {'form': f})
