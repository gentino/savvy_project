
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Withdrawal
from .forms import WithdrawalForm


# Create your views here.


@login_required
def withdraw(request):
    if request.method == "POST":
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            withdrawal = form.save(commit=False)
            withdrawal.user = request.user
            withdrawal.save()
            return redirect("withdrawal_list")
    else:
        form = WithdrawalForm()

    return render(request, "withdraw.html", {"form": form})


@login_required
def withdrawal_list(request):
    withdrawals = Withdrawal.objects.filter(user=request.user).order_by("-created_at")

    return render(
        request,
        "withdrawal_list.html",
        {"withdrawals": withdrawals},
    )


@login_required
def withdrawal_detail(request, id):
    withdrawal = get_object_or_404(
        Withdrawal,
        id=id,
        user=request.user,
    )

    return render(
        request,
        "withdrawal_detail.html",
        {"withdrawal": withdrawal},
    )