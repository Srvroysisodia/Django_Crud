from django.shortcuts import render,redirect
from EmployeeApp.models import Employee
from EmployeeApp.forms import EmployeeForm

def emp_list(request):
    employee = Employee.objects.all()
    # context={
    #     'employee':employee,
    # }
    return render (request,'emp_list.html',{'employee':employee})

# Create your views here.

# def emp_form(request):
#     if request.method == 'GET':
#         form = EmployeeForm()
#         return render(request,'emp_form.html',{'form':form})
    
#     else:
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list')

def emp_form(request,emp_id=0):
    if request.method == 'GET':
        if emp_id == 0:
            form = EmployeeForm()

        else:
            employee = Employee.objects.get(emp_id=emp_id)
            form = EmployeeForm(instance=employee)

        return render(request,'emp_form.html',{'form':form})
    else:
        if emp_id == 0:
            form = EmployeeForm(request.POST)

        else:
            employee = Employee.objects.get(emp_id=emp_id)
            form = EmployeeForm(request.POST,instance=employee)

        if form.is_valid():
            form.save()
            return redirect('list')
        
def emp_delete(request,emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    employee.delete()
    return redirect('list')