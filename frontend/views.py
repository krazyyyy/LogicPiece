from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    template_name = 'frontend/index.html'
    context = {}
    return render(request, template_name, context)

def about(request):
    template_name = 'frontend/about.html'
    context = {}
    return render(request, template_name, context)

from api.models import Contact, NewsletterSubscription
from django.contrib.sitemaps import Sitemap
from django.contrib import messages
from django.urls import reverse


class CustomSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return ['home', 'about', 'contact']

    def location(self, item):
        return reverse(item)


def contact(request):
    template_name = 'frontend/contact.html'

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        include_user_email = request.POST.get('include_user_email') == 'on'  # Check if the checkbox is checked

        # Save contact information
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            description=message,
            include_user_email=include_user_email
        )

        # Save email in NewsletterSubscription if not already exists
        if include_user_email:
            newsletter_subscription, created = NewsletterSubscription.objects.get_or_create(email=email)

        # Replace the next line with your actual logic
        print(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {message}, Include User Email: {include_user_email}")
        messages.success(request, 'Message Sent Successfully!')
        # return redirect('contact')
        # return redirect('success_page')  # Redirect to a success page after successful form submission

    return render(request, template_name)