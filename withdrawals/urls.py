from django.urls import path
from . import views

urlpatterns = [
    path("withdraw/", views.withdraw, name="withdraw"),
    path("history/", views.withdrawal_list, name="withdrawal_list"),
    path("history/<int:pk>/", views.withdrawal_detail, name="withdrawal_detail"),
]