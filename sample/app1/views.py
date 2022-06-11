from django.shortcuts import render
from.forms import studentform
from.models import student
from django.http import HttpResponse
# Create your views here.
'''def display(request):
    if request.method=='POST':
        a=(request.POST['n1'])
        b=''
        i=0
        y=len(a)
        while (i<y):
            b=a[i]+b
            i=i+1
        return render(request,'rrr.html',{'data1':b})
    else:
        return render(request,'rrr.html')
def display1(request):
    if request.method=='POST':
        a=int(request.POST['n1'])
        if a%2==0:
            x = "the number is even"
            return render(request,'rrr.html',{'data':x})
        else:
            x = "the number is odd"
            return render(request, 'rrr.html', {'data': x})
def display2(request):
    return render(request,'rrr.html')'''
'''def display(request):
    return render(request,'database.html')'''

'''def list(request):
    if request.method=='POST':
        l=[]
        a=request.POST['a1']
        b=request.POST['a2']
        c=request.POST['a3']
        d=request.POST['a4']
        l.append(a)
        l.append(b)
        l.append(c)
        l.append(d)
        return render(request,'list.html',{'data':l})
    else:
        return render(request,'list.html')'''

'''def insert(request):
    if request.method=='POST':
        a=request.POST['n1']
        b=request.POST['n2']
        c=request.POST['n3']
        data=student.objects.create(roll=a,name=b,age=c)
        data.delete()
        return HttpResponse('create')

def disp(request):
    if request.method=='GET':
        data=student.objects.all()
        return render(request,'display.html',{'r':data})
def disp1(request):
    return render(request,'newpage.html')
def search(request):
    if request.method=='POST':
        a=request.POST['a1']
        data=student.objects.filter(roll=a)
        data.delete()
        return HttpResponse("DELETED")
def update(request):
    if request.method=='POST':
        a=request.POST['n1']
        b=request.POST['n2']
        c=request.POST['n3']
        student.objects.filter(roll=a).update(name=b,age=c)
        return HttpResponse("update")'''

def display(request):
    s = studentform()
    return render(request, 'new.html', {'data': s})