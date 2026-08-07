from django.urls import path
from .import views

urlpatterns = [
    path('all',views.groups,name="groups"),
    path('create',views.create,name="create_group"),
    path('group/<int:id>',views.group_details,name="group"),
    path('delete/<int:id>',views.delete,name="delete_group")
    
]
