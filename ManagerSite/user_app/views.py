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
            cursor.execute("SELECT * FROM user_app_customuser WHERE last_name=%s OR first_name=%s OR email=%s OR telephone_number=%s", [expression])
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

    return results

def get_filtered_objects_id(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM user_app_customuser WHERE id=%s", str(expression))
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

    return results

def update_filtered_object_true(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE user_app_customuser SET is_active = True WHERE id=%s", str(expression))
        except TypeError:
            print('TypeError')

def update_filtered_object_false(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE user_app_customuser SET is_active = False WHERE id=%s", str(expression))
        except TypeError:
            print('TypeError')

def delete_object(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM client_app_task WHERE (client_id=%s OR worker_id=%s) AND status='a'", str(expression))
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None
    if len(results) != 0 or results == None:
        return False
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE client_app_task SET client_id = 1 WHERE client_id=%s", str(expression))
            cursor.execute("UPDATE client_app_task SET worker_id = 1 WHERE worker_id=%s", str(expression))
            cursor.execute("UPDATE send_contact_app SET user_id = 1 WHERE user_id=%s", str(expression))
            cursor.execute("DELETE FROM user_app_customuser WHERE id=%s", str(expression))
            results = True
        except TypeError:
            print('TypeError')
            results = False
        return results

@login_required
def list_view(request):
    if "q" in request.GET:
        expression = request.GET['q']
        objects = get_filtered_objects(expression)
        if len(objects) < 1 or objects == None:
            return redirect(to='/notfound/')
    else:
        objects = get_all_objects()
    params = {
        'objects': objects
    }
    return render(request, 'user_app/list.html', params)

@login_required
def detail_view(request, user_id):
    if request.method == 'POST':
        data = request.POST
        if data.get("is_active") == 'True':
            update_filtered_object_true(user_id)
        else:
            update_filtered_object_false(user_id)
        return redirect(to='/user-info/')
    else:
        objects = get_filtered_objects_id(user_id)
        if objects == None:
            return redirect(to='/notfound/')
        params = {
            'objects': objects
        }
        return render(request, 'user_app/detail.html', params)

@login_required
def delete_view(request, user_id):
    if delete_object(user_id):
        return redirect(to='/user-info/')
    return redirect(to='/user-info/')
