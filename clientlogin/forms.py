from dataclasses import fields
from django import forms
from expert_login.models import Files
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Row,Column,Div
class UploadForm(forms.ModelForm):
    class Meta:
        model=Files
        fields = ('fl_name','fl_description','fl_file','fl_input_file','fl_output_file')
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
     #   self.helper=FormHelper()
    #    self.helper.layout=Layout(Div(Div('fl_file', css_class='span6'),Div('fl_file', css_class='span6'),css_class='row-fluid'), 
    # )
        
