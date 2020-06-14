from django.shortcuts import render


def tires(request):
    return render(request, "tires/tires.html")
