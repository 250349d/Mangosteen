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
            cursor.execute("SELECT * FROM send_contact_app_contact WHERE id=%s", str(expression))
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

    return results

def delete_object(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("DELETE FROM send_contact_app_contact WHERE id=%s", str(expression))
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
    return render(request, 'contact_app/list.html', params)

@login_required
def detail_view(request, contact_id):
    objects = get_filtered_objects_id(contact_id)
    if objects == None:
        return redirect(to='/notfound/')
    params = {
        'objects': objects
    }
    return render(request, 'contact_app/detail.html', params)

@login_required
def delete_view(request, contact_id):
    if delete_object(contact_id):
        return redirect(to='/contact-info/')
    return redirect(to='/contact-info/')
