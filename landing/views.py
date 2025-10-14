from django.shortcuts import render

def homepage_view(request):
    return render(request, "base.html")

def s(request):
    return render(request, "services_hover.html")
