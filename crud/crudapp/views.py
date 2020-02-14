from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.
def create(request):
    stud=studentsDetail()
    if request.method=="POST":
        stud.name=request.POST['name']
        stud.age=request.POST['age']
        stud.department = request.POST['department']
        stud.address = request.POST['address']
        stud.save()
        return HttpResponse('form saved')
        # stud=studentsDetail(request.POST)
        # if stud.is_valid():
        #     stud.studentsDetail()
        #     stud.name=stud.cleaned_data('name')
    return render(request,'create.html',{'stud':stud})

def createform(request):
    showform=details()
    if request.method=="POST":
        show=details(request.POST)
        if show.is_valid():
            stud=studentsDetail()
            stud.name=show.cleaned_data['name']
            stud.age = show.cleaned_data['age']
            stud.department = show.cleaned_data['department']
            stud.address = show.cleaned_data['address']
            stud.save()
            return HttpResponse('form saved to the database')
    return render(request, 'createform.html', {'showform': showform})

def showdata(request):
    show=studentsDetail.objects.all()
    return render(request,'fetch.html',{'show':show})

def update(request,id):
    up=studentsDetail.objects.get(id=id)
    if request.method=='POST':
        up = studentsDetail.objects.get(id=id)
        up.name=request.POST['name']
        up.age = request.POST['age']
        up.department = request.POST['department']
        up.address = request.POST['address']
        up.save()
        return HttpResponse('updated')
    return render(request,'update.html',{'up':up})
def delete(request,id):
    dele=studentsDetail.objects.get(id=id)
    dele.delete()
    return HttpResponse('deleted')