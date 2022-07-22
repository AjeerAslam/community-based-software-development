from curses.ascii import HT
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Clients
from django.http import JsonResponse
from home.models import Projects


# Create your views here.
def index(request):
    #client_table=Clients.objects.raw('SELECT *,cl_id AS age FROM clients')
    #client_table=Clients.objects.all()
    projects_table=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
    return render(request,'index.html',{'Projects':projects_table})

def accept(request):
    print(request)
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        return JsonResponse({"rs": success})
        print(hello)
    

    

   