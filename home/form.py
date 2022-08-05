from django import forms
from expert_login.models import Projects
from expert_login.models import Clients
class Formsignup(forms.ModelForm):  
    class Meta:  
        model = Clients
        fields = ['cl_name','cl_email','cl_phone','cl_address','cl_password']
 
    def __init__(self, *args, **kwargs):
            super(Formsignup, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

class Requirements(forms.ModelForm):  
    class Meta:  
        model = Projects 
        fields = ['pr_name','pr_type','pr_description','pr_due']
 
    def __init__(self, *args, **kwargs):
            super(Requirements, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'


       