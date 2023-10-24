from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'frontend/index.html'
    context = {}
    return render(request, template_name, context)

def about(request):
    template_name = 'frontend/about.html'
    context = {}
    return render(request, template_name, context)

def contact(request):
    template_name = 'frontend/contact.html'
    context = {}
    return render(request, template_name, context)