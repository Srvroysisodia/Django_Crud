# Generated by Django 4.0.4 on 2022-05-10 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0009_alter_employee_emp_add_alter_employee_emp_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_add',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_awards',
            field=models.CharField(choices=[('best emp of month', 'BEOM'), ('best emp of Year', 'BEOY')], default=('best emp of month', 'BEOM'), max_length=17),
        ),
    ]