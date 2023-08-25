from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ContactForm
from .models import Sector
from .models import Update


# Create your views here.


def index(request):
    update = Update.objects.all()
    sector = Sector.objects.all()

    context = {"update": update, "sector": sector, "is_index": True}

    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about-us.html", context)


def update(request):
    update = Update.objects.all()
    context = {"update": update, "is_update": True}
    return render(request, "web/update.html", context)


def update_detail(request, id):
    update = Update.objects.get(id=id)

    context = {"update": update}
    return render(request, 'web/update-single.html', context)


def sector(request):
    sector = Sector.objects.all()
    context = {"sector": sector, "is_sector": True}
    return render(request, "web/business_sectors.html", context)


def sector_detail(request, id):
    sector = Sector.objects.get(id=id)

    context = {"sector": sector}
    return render(request, 'web/service-details.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            form.save()
            return redirect("web:contact")

    context = {"is_contact": True, "form": form}

    return render(request, 'web/contact.html', context)
