from django.shortcuts import render
from .models import *


def index(request):
    # Query data from the models
    website = Website.objects.first()
    services = Services.objects.first()
    liquidation_steps = Liquidation_Steps.objects.first()
    about_info = About.objects.first()
    team_members = AmazingTeam.objects.first()
    social_links = OurSocials.objects.first()
    privacy_policy = PrivacyPolicy.objects.first()  # Assuming only one instance
    terms_conditions = TermsAndConditions.objects.first()  # Assuming only one instance
    copyright_info = Copyright.objects.first()  # Assuming only one instance

    # If the request method is POST
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # Create a new ContactUs object
        contact = ContactUs.objects.create(
            name=name, email=email, phone=phone, message=message
        )

        contact.save()
    # Pass data to the template context
    context = {
        "services": services,
        "liquidation_steps": liquidation_steps,
        "about_info": about_info,
        "team_members": team_members,
        "social_links": social_links,
        "privacy_policy": privacy_policy,
        "terms_conditions": terms_conditions,
        "copyright_info": copyright_info,
        "website": website,
    }

    return render(request, "app/index.html", context)
