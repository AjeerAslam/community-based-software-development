from django import forms  
from expert_login.models import Modules, Projects  #models.py
     
class module_creation_form(forms.ModelForm):  
    class Meta:  
        model = Modules 
        fields = ['md_name','md_input']
 
    def __init__(self, *args, **kwargs):
            super(module_creation_form, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
class project_close_form(forms.ModelForm):  
    class Meta:  
        model = Projects 
        fields = ['pr_file','pr_closing']
 
    def __init__(self, *args, **kwargs):
            super(project_close_form, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'