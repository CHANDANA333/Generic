from django.shortcuts import render , redirect , HttpResponse


def gendes(req):
    return render(req, 'gen_desc.html' )