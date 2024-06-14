from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    queryset = Driver.objects.all()
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "drivers"
    queryset = Driver.objects.all()
    paginate_by = 5


class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer
