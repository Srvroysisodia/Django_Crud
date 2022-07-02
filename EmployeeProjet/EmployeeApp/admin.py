from django.contrib import admin
from EmployeeApp.models import Employee,Position,Nick

@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','emp_qual','emp_mobile','emp_email','emp_gender','emp_sal','emp_position','emp_add','emp_experience','emp_awards']

admin.site.register(Position)
admin.site.register(Nick)


# Register your models here.
