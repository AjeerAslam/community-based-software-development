from curses.ascii import HT
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Modules
from home.models import Clients
from django.http import JsonResponse
from home.models import Projects
from home.models import Experts

# Create your views here.

def load(request):
    
    return render(request,'expertlogin.html')

        
    
def index(request):
    #client_table=Clients.objects.raw('SELECT *,cl_id AS age FROM clients')
    #client_table=Clients.objects.all()
        username= request.POST['username']
        password = request.POST['password']
        login_details = {
         'username': username,
         'password': password
        }
        login_verification=Experts.objects.raw('SELECT * FROM experts WHERE ex_id=%s AND ex_password=%s',[username,password])
        projects_latest=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
        projects_task=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="waiting"')
        projects_review=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="review"')
        projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed"')
        modules=Modules.objects.raw('SELECT * FROM modules WHERE md_status="new"')
        modules_review=Modules.objects.raw('SELECT * FROM modules WHERE md_status="review"')
        modules_completed=Modules.objects.raw('SELECT * FROM modules WHERE md_status="completed"')
        if login_verification:
            return render(request,'index.html',{'Projects':projects_latest,'Projects_task':projects_task,'Projects_review':projects_review,'Projects_completed':projects_completed,'Modules':modules,'Modules_review':modules_review,'Modules_completed':modules_completed,'login_details':login_details})
        else:
            login_details["username"]="username/password error"
            return render(request,'expertlogin.html',{'Projects':projects_latest,'Projects_task':projects_task,'Projects_review':projects_review,'Projects_completed':projects_completed,'Modules':modules,'Modules_review':modules_review,'Modules_completed':modules_completed,'login_details':login_details})
    

def accept(request):
    print(request)
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        return JsonResponse({"rs": success})
        print(hello)
def module_creation(request):
    
    return render(request,'module_creation.html')