from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ManagerCreationForm, ManagerChangeForm

# 認証モデルを取得
Manager = get_user_model()

@login_required
def list_view(request):
    """
    管理者を取得しレンダするビュー
    クエリがある場合は条件に合ったもののみ表示する
    入力：HttpRequest
    出力：htmlファイルのレンダ
    """
    if "q" in request.GET:
        expression = request.GET['q']
        managers = Manager.objects.filter(
            Q(username=expression) |
            Q(first_name=expression) |
            Q(last_name=expression)
        ).order_by('id')
        if len(managers) < 1 or managers == None:
            return redirect(to='/notfound/')
    else:
        managers = Manager.objects.all().order_by('id')
    params = {
        'managers': managers
    }
    return render(request, 'manager_app/list.html', params)

@login_required
def detail_view(request, manager_id):
    """
    manager_id と一致する管理者の詳細情報を表示する
    また，フォームからPOSTリクエストを受け取った場合，
    対象の管理者をアクティブまたは非アクティブ状態に変更する
    入力：HttpRequest，manager_id
    出力：情報変更フォームのレンダ
    """
    manager = get_object_or_404(Manager, id=manager_id)
    if request.method == 'POST':
        form = ManagerChangeForm(request.POST, instance=manager)
        if form.is_valid():
            user = form.save()
            return redirect(to='/manager-info/')
    else:
        form = ManagerChangeForm(instance=manager)
        param = {
            'form': form,
            'manager': manager
        }
        return render(request, 'manager_app/detail.html', param)
    
@login_required
def create_view(request):
    """
    新規管理者の登録を行う
    入力：HttpRequest
    出力：情報登録フォームのレンダ
    """
    if request.method == 'POST':
        form = ManagerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="/manager-info/")
    else:
        form = ManagerCreationForm()
        param = {
            'form': form
        }
        return render(request, 'manager_app/create.html', param)
    
@login_required
def delete_view(request, manager_id):
    """
    idと一致する管理者の削除
    入力：HttpRequest，manager_id
    出力：/manager-info/へのリダイレクト
    """
    manager = get_object_or_404(Manager, id=manager_id)
    manager.delete()
    return redirect(to='/manager-info/')
