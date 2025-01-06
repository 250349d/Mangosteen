from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db import connections
from collections import namedtuple
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q

User = get_user_model()

@login_required
def list_view(request):
    groups = Group.objects.all().order_by('id')
    params = {
        'groups': groups
    }
    return render(request, 'group_app/list.html', params)

@login_required
def choice_view(request, manager_id):
    if request.method == 'POST':
        data = request.POST
        manager = get_object_or_404(User, id=manager_id)
        groups = Group.objects.all().order_by('id')
        for group in groups: # グループ数まわす
            if data.get("group") == group.name:
                manager.groups.add(Group.objects.get(name=group.name))
            else:
                manager.groups.remove(Group.objects.get(name=group.name))
        manager = get_object_or_404(User, id=manager_id)
        return redirect(to='/manager-info/')
    manager = get_object_or_404(User, id=manager_id)
    groups = Group.objects.all().order_by('id')
    params = {
        'manager': manager,
        'groups': groups
    }
    return render(request, 'group_app/choice.html', params)
