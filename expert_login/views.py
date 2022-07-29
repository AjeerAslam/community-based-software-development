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
from expert_login.forms import module_creation_form,project_close_form #forms.py
from django.shortcuts import redirect
   


# Create your views here.
def test(request):
    
    return render(request,'ex_new_modules.html')



def load(request):
    
    return render(request,'expertlogin.html')

        
    

    

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
def ex_login(request):
    return render(request,'expertlogin.html')
def ex_login_verification(request):
    #client_table=Clients.objects.raw('SELECT *,cl_id AS age FROM clients')
    #client_table=Clients.objects.all()
    username= request.POST["username"]
    password = request.POST['password']
    request.session['username'] = username
    print(request.session['username'])
    login_verification=Experts.objects.raw('SELECT * FROM experts WHERE ex_id=%s AND ex_password=%s',[username,password])
    modules=Modules.objects.raw('SELECT * FROM modules WHERE md_status="new"')
    modules_review=Modules.objects.raw('SELECT * FROM modules WHERE md_status="review"')
    modules_completed=Modules.objects.raw('SELECT * FROM modules WHERE md_status="completed"')
    if login_verification:
        projects_latest=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
        return render(request,'ex_home.html',{'Projects':projects_latest})
    else:
        return render(request,'expertlogin.html',{'error':"username/password error"})
def ex_home(request):
    projects_latest=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
    return render(request,'ex_home.html',{'Projects':projects_latest})
def ex_myworks(request):
    projects_task=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="waiting" AND pr_ex_id=%s',[request.session['username']])
    return render(request,'ex_myworks.html',{'Projects_task':projects_task})
def ex_review(request):
    projects_review=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="review"')
    return render(request,'ex_review.html',{'Projects_review':projects_review})
def ex_completed(request):
    projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed"')
    return render(request,'ex_completed.html',{'Projects_completed':projects_completed})
def accept(request):
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        return JsonResponse({"rs": 300})
def project_close(request):
    if request.method == 'GET':
        request.session['pr_id']= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        #Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        project_close = project_close_form()  
        return render(request,'project_close_form.html',{'form':project_close})
    if 'project_close' in request.POST:  
        project_close = project_close_form(request.POST, request.FILES)
        if project_close.is_valid():
            handle_uploaded_file(request.FILES['pr_file'])
            file= request.FILES["pr_file"]
            close = request.POST['pr_closing'] 
            ex_id=request.session['username']
            pr_id=request.session['pr_id']
            print(ex_id,pr_id)
            Projects.objects.filter(pr_id=pr_id,pr_ex_id=ex_id ).update(pr_file=file,pr_closing=close,pr_status='review')
            #Projects.objects.raw('UPDATE projects SET pr_file=%s AND pr_closing=%s WHERE pr_id=%s AND pr_ex_id=%s',[file,close,pr_id,ex_id])
            #model_instance = student.save(commit=False)
            #model_instance.save()
            return redirect('/ex_myworks/')
            