from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_view(request):
    if request.method == "GET":
        return HttpResponse("GET")
    elif request.method == "POST":
        print(request)
        return HttpResponse("POST")
    else:
        return HttpResponse("Method not allowed")
