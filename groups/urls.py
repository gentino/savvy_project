from django.urls import path
from .import views

urlpatterns = [
    path('groups',views.groups,name="groups"),
    path('create',views.create,name="create_group"),
    path('group/<int:id>',views.group,name="group")
]
