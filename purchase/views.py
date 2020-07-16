from django.shortcuts import render


def purchase(request):
    return render(request, "purchase/purchase.html")
