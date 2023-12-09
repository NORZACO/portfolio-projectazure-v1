from django.shortcuts import render, get_object_or_404, redirect
from bloge.models.service import (
    Service,
    Icon,
    Properties,
    Agents,
    About,
    News,
    Testimonials,
    Contact,
)  # noqa: F811
from django.core.mail import send_mail  # noqa: F401
from django.core.mail import EmailMessage  # noqa: F401
from django.conf import settings  # noqa: F401
from django.contrib import messages
from django.core.exceptions import ValidationError
import os


# index
def index(request):
    services = Service.objects.all()
    icons = Icon.objects.all()
    # only show first newest 3 properties
    properties = Properties.objects.all().order_by("-id")[:3]
    agents = Agents.objects.all()
    news = News.objects.all()
    testimonials = Testimonials.objects.all()

    context = {
        "services": services,
        "icons": icons,
        "properties": properties,
        "agents": agents,
        "news": news,
        "testimonials": testimonials,
    }
    return render(request, "realestate/index.html", context)


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Construct the email body
#         email_body = f"Name: {name}\nEmail: {email}\n\n{message}"

#         # Send an email
#         send_mail(
#             subject,
#             email_body,
#             settings.DEFAULT_FROM_EMAIL,  # Email from
#             [settings.CONTACT_EMAIL],  # Email to
#             fail_silently=False,
#         )

#         # Redirect or send a success message
#         return render(request, 'contact_success.html')  # Redirect to a success page

#     return render(request, 'contact.html')


def contact(request):
    if request.method == "POST":
        email_address = request.POST.get("email")
        username = request.POST.get("name")
        subject = request.POST.get("subject")
        phonenumber = request.POST.get("phonenumber")
        user_message = request.POST.get("message")

        # Manual validation checks
        if not user_message or not username or not subject or not email_address:
            messages.error(request, "All fields are required")
        elif "@" not in email_address:
            messages.error(request, "Invalid email address")

        # Save the contact if there are no validation errors
        if not messages.get_messages(request):
            try:
                contact = Contact(
                    name=username,
                    user_email=email_address,
                    descriptions=user_message,
                    phonenumber=phonenumber,
                    subject=subject,
                )
                contact.save()
                # Send a confirmation email to the user

                with open(
                    os.path.join(
                        settings.BASE_DIR, "email_templates", "thank_you_message.txt"
                    )
                ) as f:
                    thank_you_message = f.read()

                email = EmailMessage(
                    f"{subject}",
                    f"Dear {username}\n\n{thank_you_message}",
                    settings.DEFAULT_FROM_EMAIL,  # Email to
                    [email_address],  # Email from
                )

                email.send()

                # Send an email
                # email = EmailMessage(
                #     subject,
                #     f"Name: {username}\nEmail: {email_address}\n\n{user_message}",
                #     email_address,  # Email from
                #     [settings.DEFAULT_FROM_EMAIL],  # Email to
                #     reply_to=[email_address],
                # )
                # email.send()
                messages.success(
                    request,
                    f"Thanks your {username},  Your message has been sent successfully",
                )
                return redirect("contact")  # Redirect to clear POST data
            except ValidationError as e:
                messages.error(request, str(e))

    return render(request, "realestate/contact.html")


def about(request):
    # about
    about = About.objects.all()
    context = {"about": about}
    return render(request, "realestate/about.html", context)


def property_grid(request):
    properties = Properties.objects.all()
    context = {"properties": properties}
    print(properties)
    return render(request, "realestate/property_grid.html", context)


def property_single(request, property_id):
    # ge property by id
    property = get_object_or_404(Properties, pk=property_id)
    # pk means primary key
    context = {"property": property}
    return render(request, "realestate/property-single.html", context)


def search_properties(request):
    if request.method == "POST":
        keyword = request.POST.get("keyword")
        property_type = request.POST.get("Type")
        city = request.POST.get("city")  # noqa: F841
        bedrooms = request.POST.get("bedrooms")  # noqa: F841
        garages = request.POST.get("garages")  # noqa: F841
        bathrooms = request.POST.get("bathrooms")  # noqa: F841
        min_price = request.POST.get("price")  # noqa: F841

        # Filter properties based on the criteria
        properties = Properties.objects.all()
        if keyword:
            properties = properties.filter(
                name__icontains=keyword
            )  # Assuming 'name' contains the keyword
        if property_type and property_type != "All Type":
            properties = properties.filter(type=property_type)
        # Add more filters based on other fields like city, bedrooms, etc.

        return render(
            request, "realestate/search_results.html", {"properties": properties}
        )

    # redirect the same page if the request method is not POST
    return redirect("/")


def reviews_singele_page(request):
    return render(request, "realestate/reviews.html")


# if url does not match then it will show 404 error
def productView(request):
    return render(request, "realestate/reviews.html")
