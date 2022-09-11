from curses.ascii import HT
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from expert_login.models import Modules
from expert_login.models import Clients
from expert_login.models import Consists
from django.http import JsonResponse
from expert_login.models import Projects
from expert_login.models import Experts
from expert_login.functions import handle_uploaded_file  #functions.py
from expert_login.forms import module_creation_form,project_close_form,module_suggestion_form #forms.py
from django.shortcuts import redirect
from django.db import connection
import mimetypes
import os
from django.http.response import HttpResponse
from django.contrib.auth import logout


# Create your views here.





def load(request):
    print(5)
    return render(request,'expertlogin.html')

        
    

    

'''def accept(request):
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        return JsonResponse({"rs": success})'''
'''def module_page(request):
    return render(request,'module_page.html')'''

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

#login
def ex_login(request):
    return render(request,'expertlogin.html')
def ex_login_verification(request):
    #client_table=Clients.objects.raw('SELECT *,cl_id AS age FROM clients')
    #client_table=Clients.objects.all()
    if 'LOGIN' in request.POST:
        username= request.POST['username']
        password = request.POST['password']
        request.session['ex_username'] = username
        login_verification=Experts.objects.raw('SELECT * FROM experts WHERE ex_id=%s AND ex_password=%s',[username,password])
        
        if login_verification:
            request.session['ex_name'] =login_verification[0].ex_name
            projects_latest=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
            return render(request,'ex_home.html',{'Projects':projects_latest})
        else:
            return render(request,'expertlogin.html',{'error':"username/password error"})

    return redirect('expert:ex_home')
    
    
def log_out(request):
    logout(request)
    return redirect('expert:ex_login')

#project
def ex_home(request):
    projects_latest=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
    return render(request,'ex_home.html',{'Projects':projects_latest})
def ex_myworks(request):
    projects_task=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="waiting" AND pr_ex_id=%s',[request.session['ex_username']])
    return render(request,'ex_myworks.html',{'Projects_task':projects_task})
def ex_review(request):
    projects_review=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="review" AND pr_ex_id=%s',[request.session['ex_username']])
    return render(request,'ex_review.html',{'Projects_review':projects_review})
def ex_completed(request):
    projects_completed=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="completed" AND pr_ex_id=%s',[request.session['ex_username']])
    return render(request,'ex_completed.html',{'Projects_completed':projects_completed})

#project buttons
def accept(request):
    
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Projects.objects.filter(pr_id=id).update(pr_status='waiting',pr_ex_id=request.session['ex_username'])
        projects_latest=Projects.objects.raw('SELECT * FROM projects WHERE pr_status="new"')
        return render(request,'ex_home.html',{'Projects':projects_latest,'ok':"success"})
def description(request,pk):
    obj=Projects.objects.filter(pr_id=pk).values()
    return render(request,'description.html',{'desc':obj[0]['pr_description']})
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
            ex_id=request.session['ex_username']
            pr_id=request.session['pr_id']
            Projects.objects.filter(pr_id=pr_id,pr_ex_id=ex_id ).update(pr_file=file,pr_closing=close,pr_status='review')
            #Projects.objects.raw('UPDATE projects SET pr_file=%s AND pr_closing=%s WHERE pr_id=%s AND pr_ex_id=%s',[file,close,pr_id,ex_id])
            #model_instance = student.save(commit=False)
            #model_instance.save()
            return redirect('/expert/ex_myworks/')

#modules
def ex_new_modules(request):
    if 'id' in request.GET:
        request.session['pr_id']= request.GET.get('id')
    new_modules=Modules.objects.raw('SELECT * FROM modules WHERE md_status="new" AND md_pr_id=%s',[request.session['pr_id']])
    return render(request,'ex_new_modules.html',{'Modules_new':new_modules})
def ex_manage_modules(request):
    manage_modules=Modules.objects.raw('SELECT * FROM modules WHERE md_status="waiting" AND md_pr_id=%s',[request.session['pr_id']])
    return render(request,'ex_manage_modules.html',{'Modules_manage':manage_modules})
def ex_review_modules(request):
    review_modules=Modules.objects.raw('SELECT * FROM modules WHERE md_status="review" AND md_pr_id=%s',[request.session['pr_id']])
    return render(request,'ex_review_modules.html',{'Modules_review':review_modules})
def ex_completed_modules(request):
    completed_modules=Modules.objects.raw('SELECT * FROM modules WHERE md_status="completed" AND md_pr_id=%s',[request.session['pr_id']])
    return render(request,'ex_completed_modules.html',{'Modules_completed':completed_modules})

#modules buttons
def download_file(request):
    
    # Define Django project base directory
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename =request.session['file_name']
    # Define the full file path
    filepath = BASE_DIR + '/static/upload/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
def download_request(request):
    if request.method == 'GET':
        request.session['pr_id']= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        #Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        #projects_download=Projects.objects.raw('SELECT * FROM projects WHERE  pr_id=%s',[request.session['pr_id']])
        projects_download=Projects.objects.filter(pr_id=request.session['pr_id']).values()
        #print(projects_download)
        request.session['file_name']= projects_download[0]['pr_file']
        #print(request.session['file_name'])
        return render(request,'download.html')
def download_request_client(request):
    if request.method == 'GET':
        request.session['pr_id']= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        #Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        #projects_download=Projects.objects.raw('SELECT * FROM projects WHERE  pr_id=%s',[request.session['pr_id']])
        projects_download=Projects.objects.filter(pr_id=request.session['pr_id']).values()
        #print(projects_download)
        request.session['file_name']= projects_download[0]['pr_file']
        #print(request.session['file_name'])
        return render(request,'download_client.html')
def module_creation(request):  
    if 'module_creation_button' in request.POST:  
        module = module_creation_form(request.POST, request.FILES)
         
        if module.is_valid():
            #module.pr_ex_id=request.session['pr_id']
            #module.md_staus='new'
            handle_uploaded_file(request.FILES['md_input_file']) 
            handle_uploaded_file(request.FILES['md_output_file']) 
            md=module.save() 
            Modules.objects.filter(md_id=md.md_id).update(md_status='new',md_pr_id=request.session['pr_id'])
            #Modules.objects.raw('UPDATE modules SET md_output="new" WHERE md_id=id',[md.md_id])
            #model_instance = student.save(commit=False)
            #model_instance.save()
            return redirect('/expert/ex_new_modules/')  
    else:  
        module = module_creation_form()  
        return render(request,"module_creation.html",{'form':module})
def md_description(request,pk):
    obj=Modules.objects.filter(md_id=pk).values()
    return render(request,'description.html',{'desc':obj[0]['md_description']})

def approve_module(request):
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Modules.objects.filter(md_id=id).update(md_status='completed',md_pr_id=request.session['pr_id'])
        review_modules=Modules.objects.raw('SELECT * FROM modules WHERE md_status="review" AND md_pr_id=%s',[request.session['pr_id']])
        #tottal=Modules.objects.raw('SELECT COUNT(%s) FROM modules ',[request.session['pr_id']])
        tottal=Modules.objects.filter(md_pr_id=request.session['pr_id']).count()
        no_of_completed=Modules.objects.filter(md_pr_id=request.session['pr_id'],md_status='completed').count()
        pr_progress=(no_of_completed/tottal)*100
        Projects.objects.filter(pr_id=request.session['pr_id']).update(pr_progress=pr_progress)
        #review_modules=Modules.objects.raw('SELECT * FROM modules WHERE md_status="review" AND md_pr_id=%s',[request.session['pr_id']])
        return render(request,'ex_review_modules.html',{'Modules_review':review_modules,'ok':"success"})
       
def module_suggestion(request):
    if request.method == 'GET':
        print(100)
        request.session['md_id']= request.GET.get('id')
        print(request.session['md_id'])
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        #Projects.objects.filter(pr_id=id).update(pr_status='waiting')
        module_suggestion = module_suggestion_form()  
        return render(request,'module_suggestion_form.html',{'form':module_suggestion})
    if 'project_close' in request.POST:  
        module_suggestion = module_suggestion_form(request.POST)
        if module_suggestion.is_valid():
            md_suggestion=request.POST['md_sugg']
            md_id=request.session['md_id']
            Modules.objects.filter(md_id=md_id).update(md_status='waiting',md_sugg=md_suggestion)
            #Projects.objects.raw('UPDATE projects SET pr_file=%s AND pr_closing=%s WHERE pr_id=%s AND pr_ex_id=%s',[file,close,pr_id,ex_id])
            #model_instance = student.save(commit=False)
            #model_instance.save()
            return redirect('/expert/ex_manage_modules/')



            