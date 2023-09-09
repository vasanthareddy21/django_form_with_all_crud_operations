from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if(request.method=='POST'):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sid=SFDO.cleaned_data['Sid']
            Semail=SFDO.cleaned_data['Semail']
            SO=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            SO.save()
            # return HttpResponse('data is inserted succesfully')
        #Student.objects.filter(Sname='vasantha').update(Sid='346')
        #Student.objects.filter(Sname='mouni').update(Sname='Mounika')
        Student.objects.filter(Sname='vasantha').delete()

        QSO=Student.objects.all()
        d1={'QSO':QSO}

        return render(request,'display_student.html',d1)


    return render(request,'insert_student.html',d)
