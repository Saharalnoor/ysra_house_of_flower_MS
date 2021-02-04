from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


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
    """
    Send an email to the admin
    when site visitors send message via contact form
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    f"You've got a message from {name} ({email}) on contact form.",
                    message,
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_thankyou')
    context = {
        'contact_form': ContactForm 
    }
    return render(request, 'home/contact_us.html', context)


def contact_thankyou(request):
    """
    A view to return contact_thankyou page in order \
        to inform user that the message was succseddfully sent
    """
    return render(request, 'home/contact_thankyou.html')
