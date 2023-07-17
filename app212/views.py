from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
from .models import Blogupper

# from .models import Blogupper

# Create your views here.
# from .models import Contact


def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]

        data = Contact()
        data.name = name

        data.email = email
        data.phone = phone
        data.content = content

        data.save()
        send_mail(
            "Hello " + name,
            "Hey Thank You! for connecting with me I will message you shortly!",
            "212amiit@gmail.com",
            [email],
            fail_silently=False,
        )

    postt = Blogupper.objects.all()
    contextt = {"postt": postt}
    return render(request, "index.html", contextt)
    # return render(request, "index.html")


def blogpost(request, slug):
    postt = Blogupper.objects.filter(slug=slug).first()
    contextt = {"postt": postt}
    return render(request, "blogpost.html", contextt)
    # return render(request, "blogpost.html")
