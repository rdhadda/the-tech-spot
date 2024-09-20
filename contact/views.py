from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from profiles.models import UserProfile


def contact(request):
    """
    Contact function which takes in the ContactForm
    to allow a user to contact the store.

    """

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                'Thank you for contacting us, we will respond within 24 hours'
                )
            return redirect('home')

        else:
            messages.error(request, 'There was an error sending your enquiry. \
            Please ensure all fields are valid and try again.')
            return redirect('contact')
    else:  # Populates the form with the user details if logged in
        if request.user.is_authenticated:
            try:
                user = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(
                    initial={
                        'name': user.user.username,
                        'email': user.user.email
                    }
                )
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
        'template': template
    }

    return render(request, template, context)
