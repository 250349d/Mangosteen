from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.http import HttpResponse

CustomUser = get_user_model()

def passreset_view(request):
    if request.method == "POST":
        data=request.POST
        print(data.get("email"))
        user = get_object_or_404(CustomUser, email=data.get("email"))
        new_password = get_random_string(length=20)
        user.set_password(new_password)
        user.save()
        text = 'new password :' + new_password + ';'
#        return HttpResponse(text)
        send_mail(
            'パスワード再発行',
            text,
            'mangosteen1230@gmail.com',
            [user.email],
        )
        print(new_password)
        #sendmail()でメールを送信
        return redirect("passreset_app:done")
    else:
        return render(request, "passreset_app/password_reset_request.html")

def passreset_done_view(request):
    return render(request, "passreset_app/password_reset_done.html")
