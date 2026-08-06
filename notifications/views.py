from django.shortcuts import render,redirect , get_object_or_404
from models import Notification
from django.contrib import messages

# def groups(request):
def notifications(request):
    notifcations=Notification.objects.filter(user=request.user)
    context={
        'notifications':notifcations
    }
    return render("request", "notification/notifications.html",context)


def read(request,id):
    notification=get_object_or_404(Notification,id=id)
    notification.status=True
    context={
        'notification':notification
    }
    return render("request", "notification/notification.html",context)


def delete(request,id):
    notification=get_object_or_404(Notification,id=id)
    notification.delete()
    messages.success(request,'Notification Deleted')
    return redirect('notifications')
