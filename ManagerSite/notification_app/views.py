from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Notification
from .forms import NotificationForm

@login_required
def list_view(request):
    """
    お知らせ情報を取得するビュー
    入力：HttpRequest
    出力：htmlファイルのレンダ
    """
    if "q" in request.GET:
        expression = request.GET['q']
        notifications = Notification.objects.filter(
            title=expression
        ).order_by('id')
        if len(notifications) < 1 or notifications == None:
            return redirect(to='/notfound/')
    else:
        notifications = Notification.objects.all().order_by('id')
    params = {
        'notifications': notifications
    }
    return render(request, 'notification_app/list.html', params)

@login_required
def detail_view(request, notification_id):
    """
    お問い合わせの詳細情報の取得
    入力：HttpRequest，notification_id
    出力：情報編集フォームのレンダ
    """
    notification = get_object_or_404(Notification, id=notification_id)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            notification = form.save()
            return redirect(to='/notification-info/')
    else:
        form = NotificationForm(instance=notification)
        param = {
            'form': form,
            'notification': notification
        }
        return render(request, 'notification_app/detail.html', param)
 
@login_required
def create_view(request):
    """
    新規お問い合わせの作成
    入力：HttpRequest
    出力：情報入力フォームのレンダ
    """
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="/notification-info/")
    else:
        form = NotificationForm()
        param = {
            'form': form
        }
        return render(request, 'notification_app/create.html', param)
    
@login_required
def delete_view(request, notification_id):
    """
    お問い合わせ情報の削除
    入力：HttpRequest，notification_id
    出力：/notification-info/へのリダイレクト
    """
    notification = Notification.objects.get(id=notification_id)
    notification.delete()
    return redirect(to='/notification-info/')
