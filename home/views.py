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
    projects_latest=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
    projects_task=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="waiting"')
    projects_review=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="review"')
    projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed"')
    projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed"')
    projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed"')
    projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed"')
    return render(request,'index.html',{'Projects':projects_latest,'Projects_task':projects_task,'Projects_review':projects_review,'Projects_completed':projects_completed})

def accept(request):
    print(request)
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        return JsonResponse({"rs": success})
        print(hello)
    

    

   