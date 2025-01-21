from django.shortcuts import render, redirect
from django.db import connections
from collections import namedtuple
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple("object", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def get_filtered_objects(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM client_app_transaction WHERE task_id=%s", [str(expression)])
            results = namedtuplefetchall(cursor)
        except TypeError:
            print('TypeError')
            results = None

    return results

def update_payment_client_true(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE client_app_transaction SET payment_fee_date=now() WHERE task_id=%s", [str(expression)])
            cursor.execute("UPDATE client_app_transaction SET pay_fee=True WHERE task_id=%s", [str(expression)])
        except TypeError:
            print('TypeError')

def update_payment_client_false(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE client_app_transaction SET payment_fee_date=null WHERE task_id=%s", [str(expression)])
            cursor.execute("UPDATE client_app_transaction SET pay_fee=False WHERE task_id=%s", [str(expression)])
        except TypeError:
            print('TypeError')

def update_payment_worker_true(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE client_app_transaction SET  courier_item_payment_date=now() WHERE task_id=%s", [str(expression)])
            cursor.execute("UPDATE client_app_transaction SET  pay_courier_item=True WHERE task_id=%s", [str(expression)])
        except TypeError:
            print('TypeError')

def update_payment_worker_false(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE client_app_transaction SET  courier_item_payment_date=null WHERE task_id=%s", [str(expression)])
            cursor.execute("UPDATE client_app_transaction SET  pay_courier_item=False WHERE task_id=%s", [str(expression)])
        except TypeError:
            print('TypeError')

def update_reward_true(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE client_app_transaction SET courier_reward_date=now() WHERE task_id=%s", [str(expression)])
            cursor.execute("UPDATE client_app_transaction SET pay_courier_reward=True WHERE task_id=%s", [str(expression)])
        except TypeError:
            print('TypeError')

def update_reward_false(expression):
    with connections["user_data"].cursor() as cursor:
        try:
            cursor.execute("UPDATE client_app_transaction SET  courier_reward_date=null WHERE task_id=%s", [str(expression)])
            cursor.execute("UPDATE client_app_transaction SET  pay_courier_reward=False WHERE task_id=%s", [str(expression)])
        except TypeError:
            print('TypeError')

@login_required
def detail_view(request, task_id):
    if request.method == 'POST':
        data = request.POST
        if data.get("payment_client") == 'True':
            update_payment_client_true(task_id)
        else:
            update_payment_client_false(task_id)
        if data.get("payment_worker") == 'True':
            update_payment_worker_true(task_id)
        else:
            update_payment_worker_false(task_id)
        if data.get("reward") == 'True':
            update_reward_true(task_id)
        else:
            update_reward_false(task_id)
        return redirect('task_app:list')
    else:
        objects = get_filtered_objects(task_id)
        if objects == None:
            return redirect(to='/notfound/')
        params = {
            'objects': objects
        }
        return render(request, 'transaction_app/detail.html', params)
