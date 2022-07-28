from curses.ascii import HT
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Modules
from home.models import Clients
from django.http import JsonResponse
from home.models import Projects
from home.models import Experts
from expert_login.functions import handle_uploaded_file  #functions.py
from expert_login.forms import module_creation_form #forms.py
   


# Create your views here.

'''def load(request):
    
    return render(request,'expertlogin.html')'''

        
    
def index(request):
    #client_table=Clients.objects.raw('SELECT *,cl_id AS age FROM clients')
    #client_table=Clients.objects.all()
        username= request.POST["uname"]
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
        print(projects_task)
        print(projects_task)
        if login_verification:
            print("hello")
            return render(request,'index.html',{'Projects':projects_latest,'Projects_task':projects_task,'Projects_review':projects_review,'Projects_completed':projects_completed,'Modules':modules,'Modules_review':modules_review,'Modules_completed':modules_completed,'login_details':login_details})
        else:
            login_details["username"]="username/password error"
            return render(request,'expertlogin.html',{'Projects':projects_latest,'Projects_task':projects_task,'Projects_review':projects_review,'Projects_completed':projects_completed,'Modules':modules,'Modules_review':modules_review,'Modules_completed':modules_completed,'login_details':login_details})
    

def accept(request):
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        return JsonResponse({"rs": success})
        print(hello)
def module_creation(request):
    
    return render(request,'module_creation.html')
def file(request):  
    if request.method == 'POST':  
        module = module_creation_form(request.POST, request.FILES)
         
        if module.is_valid():
            
            handle_uploaded_file(request.FILES['md_input']) 
            module.save() 
            #model_instance = student.save(commit=False)
            #model_instance.save()
            return HttpResponse("File uploaded successfuly")  
    else:  
        module = module_creation_form()  
        return render(request,"file.html",{'form':module})
'''def file(request):
      
    return render(request,'file.html')
def file_upload(request):
    handle_uploaded_file(request.FILE['myfile'])
    print (hello)
    return render(request,'file.html')'''

'''def handle_uploaded_file(f):  
    with open('myapp/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)'''

def ex_home(request):
    projects_latest=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
    return render(request,'ex_home.html',{'Projects':projects_latest})
def ex_myworks(request):
    projects_task=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="waiting"')
    return render(request,'ex_myworks.html',{'Projects_task':projects_task})
def ex_review(request):
    projects_review=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="review"')
    return render(request,'ex_review.html',{'Projects_review':projects_review})
def ex_completed(request):
    projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed"')
    return render(request,'ex_completed.html',{'Projects_completed':projects_completed})
def accept(request):
    if request.method == 'GET':
        print(5)
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        return JsonResponse({"rs": success})