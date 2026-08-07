from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import Group
from django.contrib import messages
from .forms import GroupForm
from django.contrib import messages

def groups(request):
    groups = get_list_or_404(Group,creator=request.user)
    context = {
         'groups':groups
    }
    return render(request, "group/groups.html",context)

def create(request):
    if request.method == "POST":
        form=GroupForm(request.POST,request.FILES)
        if form.is_valid():
            account= form.save(commit=False)
            account.creator=request.user
            account.save()
            messages.success(request,"Group successfully created!!!")
            return redirect('groups')
    else:
        form=GroupForm()

    context={
        'form':form
    }
    return render(request, "group/create_group.html",context)


def group_details(request, id):
    group = get_object_or_404(Group,id=id)
    context = {
        'group':group
    }
    return render(request, "group/group.html",context)

def delete(request,id):
    group =get_object_or_404(Group,id=id)
    group.delete()
    messages.success(request,'Group deleted successfully')
    return redirect('groups')


def edit_group(request,id):
    pass
    
