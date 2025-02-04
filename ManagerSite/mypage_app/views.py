from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def mypage_view(request):
    return render(request, 'mypage_app/mypage.html')
