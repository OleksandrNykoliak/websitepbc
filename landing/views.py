from django.shortcuts import render

def homepage_view(request):
    return render(request, "base.html")

# def projects_view(request):
#     return render(request, "projects.html")

# def about_view(request):
#     return render(request, "about.html")


# def about2_view(request):
#     return render(request, "about2.html")

# def services_view(request):
#     return render(request, "services.html")


# def team_view(request):
#     return render(request, "team.html")


# def customer_view(request):
#     return render(request, "customers.html")


# def contact_view(request):
#     return render(request, "contact.html")
