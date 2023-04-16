from django.shortcuts import render , redirect , HttpResponse


def dets(req):
    return render(req, 'dets.html' )