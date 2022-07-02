from django import forms
from django.forms.widgets import NumberInput,TextInput,EmailInput,Textarea
from EmployeeApp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id','emp_name','emp_qual','emp_mobile','emp_email','emp_gender','emp_sal','emp_position','emp_add','emp_experience','emp_awards','emp_nick']
        labels={
            'emp_id':'Employee ID',
            'emp_name':'Employee Name',
            'emp_qual':'Employee Qualification',
            'emp_mobile':'Employee Mobile No.',
            'emp_email': 'Employee Email',
            'emp_gender':'Employee Gender',
            'emp_sal':'Employee Position',
            'emp_position':'Employee Post',
            'emp_add':'Employee Address:',
            'emp_experience':'Employee Experience',
            'emp_awards':'Employee Awards',
            'emp_nick':'Employee Nick'
        }
        widgets={
            'emp_name':TextInput(attrs={'placeholder':'Enter Your Name'}),
            'emp_mobile':TextInput(attrs={'placeholder':'Enter Your Mobile Number'})
        }
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['emp_position'].empty_label='Select'
        self.fields['emp_nick'].empty_label='Select'

