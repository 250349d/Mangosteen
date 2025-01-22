from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse

from client_app.models import Task

CustomUser = get_user_model()

@login_required
def userdelete_view(request):
    user = get_object_or_404(CustomUser, id=request.user.id) # 対象ユーザの抽出
    if len(Task.objects.exclude(status="4").exclude(status="C").filter(client=request.user)) == 0 and len(Task.objects.exclude(status="4").exclude(status="C").filter(worker=request.user)) == 0:
        logout(request)
        user.delete()
        return redirect('home_app:homepage')
    else:
        return redirect('/cant-delete-user/')
