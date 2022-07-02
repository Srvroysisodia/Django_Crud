from django.urls import path
from EmployeeApp import views

urlpatterns = [

    path('list',views.emp_list,name='list'),
    path('',views.emp_form,name='form'),
    path('<int:emp_id>',views.emp_form,name='edit'),

    path('delete/<int:emp_id>',views.emp_delete,name='delete')
    
]
