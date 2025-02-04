from django.shortcuts import render, redirect
from django.db import connections
from collections import namedtuple
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple("object", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def get_all_objects():
    with connections["user_data"].cursor() as cursor:
        cursor.execute("SELECT * FROM user_app_customuser ORDER BY id ASC")
        results = namedtuplefetchall(cursor)

    return results

def get_filtered_objects(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM user_app_customuser WHERE last_name=%s OR first_name=%s OR email=%s OR telephone_number=%s", [expression, expression, expression, expression])
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

    return results

def get_filtered_objects_id(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM user_app_customuser WHERE id=%s", [str(expression)])
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

    return results

def update_filtered_object_true(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE user_app_customuser SET is_active = True WHERE id=%s", [str(expression)])
        except TypeError:
            print('TypeError')

def update_filtered_object_false(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE user_app_customuser SET is_active = False WHERE id=%s", [str(expression)])
        except TypeError:
            print('TypeError')

def delete_object(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM client_app_task WHERE (client_id=%s OR worker_id=%s) AND (status='0' OR status='1' OR status='2' OR status='3')", [str(expression), str(expression)])
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = -1
    if not(results==None or len(results) < 1):
        return -1
    with connections["user_data"].cursor() as cursor:
        """
        update & delete
        """
        try:
            cursor.execute("UPDATE client_app_task SET client_id = 1 WHERE client_id=%s", [str(expression)])
            cursor.execute("UPDATE client_app_task SET worker_id = 1 WHERE worker_id=%s", [str(expression)])
            cursor.execute("UPDATE send_contact_app_contact SET user_id = 1 WHERE user_id=%s", [str(expression)])
            cursor.execute("DELETE FROM user_app_customuser WHERE id=%s", [str(expression)])
            results = 1
        except TypeError:
            print('TypeError')
            results = -1
        return results

@login_required
def list_view(request):
    manager = request.user
    if "q" in request.GET:
        if request.GET['q'] == "":
            objects = get_all_objects()
        else:
            expression = request.GET['q']
            objects = get_filtered_objects(expression)
    else:
        objects = get_all_objects()

    department_groups = manager.groups.all()
    params = {
        'department_groups': department_groups,
        'objects': objects
    }
    return render(request, 'user_app/list.html', params)

@login_required
def detail_view(request, user_id):
    objects = get_filtered_objects_id(user_id)
    if objects == None or len(objects) < 1:
        return redirect(to='/notfound/')
    for object in objects:
        if object.first_name == "None":
            return redirect(to='/deleted/')
    if request.method == 'POST':
        data = request.POST
        if data.get("is_active") == 'True':
            update_filtered_object_true(user_id)
        else:
            update_filtered_object_false(user_id)
        return redirect(to='/user-info/')
    else:
        manager = request.user
        department_groups = manager.groups.all()
        params = {
            'department_groups': department_groups,
            'objects': objects
        }
        return render(request, 'user_app/detail.html', params)

@login_required
def delete_view(request, user_id):
    objects = get_filtered_objects_id(user_id)
    if objects == None or len(objects) < 1:
        return redirect(to='/notfound/')
    for object in objects:
        if object.first_name == "None":
            return redirect(to='/deleted/')
    if delete_object(user_id) < 0:
        return HttpResponse("配達中の依頼があり，削除できません")
    return redirect('user_app:list')
