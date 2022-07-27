from curses.ascii import HT
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Modules
from home.models import Clients
from django.http import JsonResponse
from home.models import Projects


# Create your views here.
def index(request):
    #client_table=Clients.objects.raw('SELECT *,cl_id AS age FROM clients')
    #client_table=Clients.objects.all()
    if request.method == 'GET':
        #id= request.GET.get('user_name')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        return JsonResponse({"rs": id})
        print(hello)
    projects_latest=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
    projects_task=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="waiting"')
    projects_review=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="review"')
    projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed"')
    modules=Modules.objects.raw('SELECT * FROM modules WHERE md_status="new"')
    modules_review=Modules.objects.raw('SELECT * FROM modules WHERE md_status="review"')
    modules_completed=Modules.objects.raw('SELECT * FROM modules WHERE md_status="completed"')
    return render(request,'index.html',{'Projects':projects_latest,'Projects_task':projects_task,'Projects_review':projects_review,'Projects_completed':projects_completed,'Modules':modules,'Modules_review':modules_review,'Modules_completed':modules_completed})

def accept(request):
    print(request)
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        return JsonResponse({"rs": success})
        print(hello)
    

    

   