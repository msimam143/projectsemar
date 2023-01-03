from django.shortcuts import render,redirect
from django.contrib import messages
from . import models
from . import forms

def index(request):
    data_artikel = models.artikel.objects.all().order_by('-id')
    context = {
        'halaman':'list artikel',
        'data':data_artikel,
    }
    return render(request,'blog/index.html',context)

def show(request,blogslug):
    if request.method=='POST':
        models.komen.objects.create(
            artikel = request.POST['kode'],
            email = request.POST['email'],
            isi = request.POST['isi']
        )
        messages.success(request,'komentar di simpan')
        return redirect('blog:show',blogslug)
    data_artikel = models.artikel.objects.get(slug=blogslug)
    context = {
        'formnya':forms.komen_Form(),
        'halaman':'detail artikel',
        'data':data_artikel,
    }    
    return render(request,'blog/show.html',context)