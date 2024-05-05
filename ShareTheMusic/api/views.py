from django.shortcuts import render
from django.http import HttpResponse

def main(request): #urls will point to this func to display, urlsSTM -> urlsAPI -> views.main
    return HttpResponse("Hello")
