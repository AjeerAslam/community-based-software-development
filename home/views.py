import email
from multiprocessing import context
from sre_constants import SUCCESS
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from .form import Formsignup, Requirements
from expert_login.models import Modules
from expert_login.models import Clients
from django.http import JsonResponse
from expert_login.models import Projects
from expert_login.models import Experts
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def test(request):
    module = Requirements()     
    return render(request,'cl_requirement.html',{'form':module})



def communitysignup(request):
    if "btn" in request.POST :
        module = Formsignup(request.POST)
        if module.is_valid():
             
            md=module.save()
            print(md.cl_id)
            return HttpResponse("data submitted successfully")    
    else:
        module = Formsignup() 
        return render(request, "communitysignup.html", {'form':module})

        
 

def login(request):
    if 'cl_login' in request.POST :
        username = request.POST['username']
        password = request.POST['password']
        request.session['username']=username
        login_verification=Clients.objects.raw('SELECT * FROM clients WHERE cl_id=%s AND cl_password=%s' ,[username,password]) 
        request.session['name']=login_verification[0].cl_name
    if login_verification:
        projects_progress=Projects.objects.raw('SELECT * FROM projects WHERE (pr_status="waiting" OR pr_status="new") AND (pr_cl_id=%s)',[request.session['username']])
        return render(request,'client_progress.html',{'Projects':projects_progress})
    else:
        return render(request,'index.html',{'error':"username/password error"})

def client_progress(request):
    projects_progress=Projects.objects.raw('SELECT * FROM projects WHERE (pr_status="waiting" OR pr_status="new") AND (pr_cl_id=%s)',[request.session['username']])
    return render(request,'client_progress.html',{'Projects':projects_progress})

def cl_requirement(request):
    if "btn1" in request.POST :
        project = Requirements(request.POST)
       
        if project.is_valid():
            
            pr=project.save()
            #Projects.objects.raw('UPDATE projects SET pr_status="new" AND pr_cl_id=%s WHERE pr_id=%s',[request.session['username'],pr.pr_id])
            Projects.objects.filter(pr_id=pr.pr_id).update(pr_status='new',pr_cl_id=request.session['username'])

            
            return HttpResponse("data submitted successfully") 

    project = Requirements()     
    return render(request,'cl_requirement.html',{'form':project})


def cl_review(request):    
        projects_review=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="review" AND pr_cl_id=%s',[request.session['username']])
        return render(request,'cl_review.html',{'Projects_review':projects_review})


def cl_completed(request):        
        projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed" AND pr_cl_id=%s',[request.session['username']])
        return render(request,'cl_completed.html',{'Projects_completed':projects_completed})
    

            
def accept(request):
    
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='completed')
        projects_review=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="review" AND pr_cl_id=%s',[request.session['username']])
        return render(request,'cl_review.html',{'Projects_review':projects_review})
def log_out(request):
    logout(request) 
    return redirect('home')

    

    

   