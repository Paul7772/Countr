from django.http import HttpResponse
from django.shortcuts import render


def views(reqest):
    return HttpResponse('<h1> print("hello, world!") </h1>')
