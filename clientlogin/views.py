from genericpath import exists
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from expert_login.models import Developers,Modules,Files
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import JsonResponse
from .forms import UploadForm



def index1(request):
    print(300)
    try :
        
        username=request.session['Email']
        if username is not None:
            id1=Developers.objects.values_list('dev_id', flat=True).get(dev_email=username)
            module_latest=Modules.objects.raw('SELECT * FROM modules WHERE md_status="new"')
            return render(request,'clientlogin/cm_home.html',{'Modules':module_latest})
            #return render(request,'clientlogin/communitylogin.html',{'Modules':module_latest})
        else:
            return render(request,'clientlogin/communitylogin.html')
            
    except :  
        errormessage="please login"
        return render(request,'clientlogin/communitylogin.html',{'error':errormessage})
        #return render(request,'clientlogin/cm_home.html',{'error':errormessage})

def cm_mywork(request):
    try:
        
        username=request.session['Email']
        if username is not None:
            id1=Developers.objects.values_list('dev_id', flat=True).get(dev_email=username)
            module_waiting=Modules.objects.raw('SELECT * FROM modules WHERE md_status="waiting" AND md_dev_id=%s',[id1])
            return render(request,'clientlogin/cm_mywork.html',{'module_waiting':module_waiting})
        else:
            return render(request,'clientlogin/communitylogin.html')
            
    except : 
        return render(request,'clientlogin/communitylogin.html',{'error':"please login"})
def cm_completed(request):
    try:
        
        username=request.session['Email']
        if username is not None:
            id1=Developers.objects.values_list('dev_id', flat=True).get(dev_email=username)
            module_completed=Modules.objects.raw('SELECT * FROM modules WHERE md_status="completed" AND md_dev_id=%s',[id1])
            return render(request,'clientlogin/cm_completed.html',{'module_completed':module_completed})
        else:
            return render(request,'clientlogin/communitylogin.html')
            
    except : 
        
        return render(request,'clientlogin/communitylogin.html',{'error':"please login"})

def cm_review(request):
    try :
        
        username=request.session['Email']
        if username is not None:
            id1=Developers.objects.values_list('dev_id', flat=True).get(dev_email=username)
            module_review=Modules.objects.raw('SELECT * FROM modules WHERE md_status="review" AND md_dev_id=%s',[id1])
            return render(request,'clientlogin/cm_riview.html',{'module_review':module_review})
        else:
            return render(request,'clientlogin/communitylogin.html')
            
    except : 
        return render(request,'clientlogin/communitylogin.html',{'error':"please login"})       

   
   

# Create your views here.
#def load(request):
    #print(200)
    
    #return render(request,'clientlogin/communitylogin.html')
def index(request):
        print(400)
 
        username= request.POST['username']
        password = request.POST['password']
       
        try:
            user=Developers.objects.get(dev_email=username,dev_password=password)
       
            
        except Developers.DoesNotExist:
            user = None
        
        if user is not None:
           
            auth1=authenticate(dev_email=username,dev_password=password)
            request.session['Email']=username
            request.session['id']=Developers.objects.values_list('dev_id', flat=True).get(dev_email=username)
            request.session['username']=Developers.objects.values_list('dev_name', flat=True).get(dev_email=username)

            
            return redirect('community:index1')
           
        
        else:
            messages.success(request,"username password doesnt match")
            return render(request,'clientlogin/communitylogin.html')

      
def logout1(request):
    
    try:    
        del request.session['Email']
        del request.session['username']
        del request.session['id']

    except:
        return render(request,'clientlogin/communitylogin.html') 
    logout(request)   
    
  
    return render(request,'clientlogin/communitylogin.html') 
         
     
def cosignup(request):
    
    return render(request,'clientlogin/communitysignup.html') 

def load(request):
    print(100)
    
    return render(request,'clientlogin/communitylogin.html')
def csignup(request):
    if request.method== 'POST' :
        username= request.POST['Name']
        email= request.POST['Email']
        cpassword = request.POST['p1']
        password = request.POST['p']
        phone= request.POST['phn']
        address=request.POST.get('add')
        value={'username':username,
            'email':email,
            'cpassword':cpassword,
            'password':password,
            'phone':phone,
            'address':address

        }
        dev=Developers(dev_name=username,dev_email=email,dev_phone=phone,dev_address=address,dev_password=password)
        errormessage=None
        
        if username=='' or email=='' or password=='' or phone=='' or address=='':
           errormessage="**ALL FIELD MUST BE FILLED***"         
        elif len(username)<5:
           errormessage="**USER NAME MUST BE GREATER THAN 5***"
          
        elif len(password)<8:
           errormessage="**PASSWORD NAME MUST BE GREATER THAN 8***"
           
        elif password!=cpassword:
           errormessage="**PASSWORD and Confirm password must be same***"
            
        elif len(phone)<10:          
            errormessage="**ENTER A VALID PHONE NUMBER***"
            
        elif dev.isExists():
            errormessage="**USER EMAIL ALREADY REGISTERED***"
            

        if not errormessage:
            dev.register()
            errormessage="SUCCESSFULLY REGISTERD"
            return render(request,'clientlogin/communitylogin.html',{'error1':"SUCCESSFULLY REGISTERD"}) 
                       
        else:
            data = {
                 'error' :errormessage,
                 'values':value
            }

            return render(request,'clientlogin/communitysignup.html',data) 
    else:
       
        return render(request,'clientlogin/communitysignup.html')      


def accept(request):
    print(request)
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Modules.objects.filter(md_id=id).update(md_status='waiting',md_dev_id=request.session['id'])
        return JsonResponse({"rs": success})
    else:
        return redirect('index1')

def cm_close(request):
    print(request)
    if request.method == 'GET':
        id= request.GET.get('id')
        #Projects.objects.raw('UPDATE projects SET pr_status="waiting" WHERE pr_id=id')
        Modules.objects.filter(md_id=id).update(md_status='review',md_dev_id=request.session['id'])
        return JsonResponse({"rs": success})
    else:
        return redirect('index1')
def cm_view(request,pk):
    files=Files.objects.all().filter(fl_md_id=pk)
    request.session['md_id']=pk
    return render(request,'clientlogin/viewmodule.html',{'files':files}) 
def ex_view(request,pk):
    files=Files.objects.all().filter(fl_md_id=pk)
    request.session['md_id']=pk
    return render(request,'clientlogin/viewmodule2.html',{'files':files})     

def cm_upload(request):
    print (request.session['md_id'])
    if request.session['md_id'] is not None:
        if request.method=='POST':
            form=UploadForm(request.POST,request.FILES);
            print("hello")    
            if form.is_valid():
                form = form.save(commit=False)
                form.fl_md_id = request.session['md_id']
                form.save()
                return redirect('community:cm_view',pk=request.session['md_id'])
            #,{'form':form}  
            else:
                return render(request,'clientlogin/upload.html',{'form':form})
        else: 
            form=UploadForm()
            return render(request,'clientlogin/upload.html',{'form':form})        #   
    else:
         return redirect('index1')
   
def cm_delete(request,pk):
    if request.method=='POST':       
        files=Files.objects.get(pk=pk)
        files.delete()
    return redirect('community:ex_view',pk=request.session['md_id'])
#def cm_view(request):
 #   if request.method=='GET':
  #          id= request.GET.get('id')
   #         request.session['md_id']=id
    #        form=UploadForm();
     #       print("hello") 
      #      print (form)
       #     print("hello")
        #    return render(request,'clientlogin/upload.html',{'form':form})
        #else:
         #   return render(request,'clientlogin/cm_mywork1.html')  
   # files=Files.objects.all()
    #return render(request,'clientlogin/viewmodule.html',{'files':files})             
          


