from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import About

# Create your views here.
def about(request):
    #return HttpResponse("This is the about page")
    # grab the most recent about object
    about_object = About.objects.order_by('-updated_on').first()
    if about_object is None:
        raise Http404("No about page found.")
    # pass to render
    return render(
        request,
        "about/about.html",
        {"about": about_object},
    )