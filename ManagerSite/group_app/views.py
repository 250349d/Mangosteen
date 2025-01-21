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
    manager = request.user
    department_groups = manager.groups.all()
    params = {
        'groups': groups,
        'department_groups': department_groups
    }
    return render(request, 'group_app/list.html', params)

@login_required
def choice_view(request, manager_id):
    manager = get_object_or_404(User, id=manager_id)
    groups = Group.objects.all().order_by('id')
    if request.method == 'POST':
        request_groups = request.POST.getlist("group")
        manager.groups.clear()
        for i in range(len(request_groups)):
            manager.groups.add(Group.objects.get(name=request_groups[i]))
        return redirect('manager_app:list')
    department_groups = manager.groups.all()
    params = {
        'manager': manager,
        'department_groups': department_groups,
        'groups': groups
    }
    return render(request, 'group_app/choice.html', params)
