from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={
        'halaman':'home',
        'deskripsi':'ini adalah halaman home',
    }
    return render(request,'index.html',context)

def about(request):
    context={
        'halaman':'about',
        'deskripsi':'ini adalah halaman about',
    }
    return render(request,'about.html',context)