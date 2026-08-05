from django.shortcuts import render

# Create your views here.

def groups(request):
    return render('request','group/groups.html')

def create(request):
    return render(request,'group/create_group.html')

def group(request,id):
    return render(request,'group/group.html')