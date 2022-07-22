from curses.ascii import HT
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Clients
from django.http import JsonResponse


# Create your views here.
def index(request):
    client_table=Clients.objects.raw('SELECT *,cl_id AS age FROM clients')
    #client_table=Clients.objects.all()
    return render(request,'index.html',{'Clients':client_table})

def edit_profile(request):
    print(request)
    if request.method == 'GET':
        id= request.GET.get('id')
        return JsonResponse({"foo": id})
        print(9)
    

    

   