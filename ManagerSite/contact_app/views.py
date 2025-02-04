from django.shortcuts import render, redirect, get_object_or_404
from django.db import connections
from collections import namedtuple
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

CustomManager = get_user_model()

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple("object", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def get_all_objects():
    with connections["user_data"].cursor() as cursor:
        cursor.execute("SELECT * FROM send_contact_app_contact ORDER BY id ASC")
        results = namedtuplefetchall(cursor)

    return results

def get_filtered_objects(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM send_contact_app_contact WHERE title=%s", [expression])
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

    return results

def get_filtered_objects_id(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM send_contact_app_contact WHERE id=%s", [str(expression)])
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

    return results

def delete_object(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("DELETE FROM send_contact_app_contact WHERE id=%s", [str(expression)])
        except TypeError:
            print('TypeError')

@login_required
def list_view(request):
    manager = request.user
    department_groups = manager.groups.all()
    if "q" in request.GET:
        if request.GET['q'] == '':
            objects = get_all_objects()
        else:
            expression = request.GET['q']
            objects = get_filtered_objects(expression)
    else:
        objects = get_all_objects()
    params = {
        'department_groups': department_groups,
        'objects': objects
    }
    return render(request, 'contact_app/list.html', params)

@login_required
def detail_view(request, contact_id):
    if not request.user.has_perm('manager_app.contact_detail'):
        return redirect('forbidden')
    objects = get_filtered_objects_id(contact_id)
    if objects == None or len(objects) < 1:
        return redirect("/notfound/")
    manager = request.user
    department_groups = manager.groups.all()
    if len(objects) < 1:
        return redirect(to='/notfound/')
    params = {
        'department_groups': department_groups,
        'objects': objects
    }
    return render(request, 'contact_app/detail.html', params)

@login_required
def delete_view(request, contact_id):
    if not request.user.has_perm('manager_app.contact_delete'):
        return redirect('forbidden')
    delete_object(contact_id)
    return redirect(to='/contact-info/')
