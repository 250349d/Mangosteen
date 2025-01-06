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
        cursor.execute("SELECT * FROM client_app_task ORDER BY id ASC")
        results = namedtuplefetchall(cursor)

    return results

def get_filtered_objects(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM client_app_task WHERE title=%s", [expression])
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

    return results

def get_filtered_objects_client(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM client_app_task WHERE client_id=%s", str(expression))
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None
    return results

def get_filtered_objects_worker(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM client_app_task WHERE worker_id=%s", str(expression))
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None
    return results

def get_filtered_objects_id_task(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM client_app_task WHERE id=%s", str(expression))
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

        return results

def get_filtered_objects_id_order(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM client_app_order WHERE task_order_id=%s", str(expression))
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

        return results

def get_filtered_objects_id_request(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM client_app_request WHERE task_request_id=%s", str(expression))
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None
        return results

def delete_object(expression):
    with connections['user_data'].cursor() as cursor:
        try:
            cursor.execute("DELETE FROM client_app_request WHERE task_request_id=%s", str(expression))
            cursor.execute("DELETE FROM chat_app_massage WHERE massage_task_id=%s", str(expression))
            cursor.execute("DELETE FROM client_app_transaction WHERE task_id=%s", str(expression))
            cursor.execute("DELETE FROM client_app_order WHERE task_order_id=%s", str(expression))
            cursor.execute("DELETE FROM client_app_task WHERE id=%s", str(expression))
        except TypeError:
            print('TypeError')

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
    return render(request, 'task_app/list.html', params)

@login_required
def detail_view(request, task_id):
    objects = get_filtered_objects_id_task(task_id)
    objects2 = get_filtered_objects_id_order(task_id)
    objects3 = get_filtered_objects_id_request(task_id)
    params = {
        'objects': objects,
        'objects2': objects2,
        'objects3': objects3
    }
    return render(request, 'task_app/detail.html', params)

@login_required
def delete_view(reqest, task_id):
    delete_object(task_id)
    return redirect(to='/task-info/')
