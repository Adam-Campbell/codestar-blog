from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from .models import About, CollaborateRequest
from .forms import CollaborateForm

# Create your views here.
def about(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        collaborate_form = CollaborateForm(request.POST)
        # check whether it's valid:
        if collaborate_form.is_valid():
            # process the data in form.cleaned_data as required
            collaborate_form.save()
            # redirect to a new URL:
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )
    
    # grab the most recent about object
    about_object = About.objects.order_by('-updated_on').first()
    if about_object is None:
        raise Http404("No about page found.")
    # pass to render
    collaborate_form = CollaborateForm()
    return render(
        request,
        "about/about.html",
        {
            "about": about_object,
            "collaborate_form": collaborate_form,
        },
    )