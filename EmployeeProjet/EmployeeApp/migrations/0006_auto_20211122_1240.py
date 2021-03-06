# Generated by Django 3.2.8 on 2021-11-22 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0005_auto_20211122_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_awards',
            field=models.CharField(choices=[('best emp of month', 'BEOM'), ('best emp of Year', 'BEOY')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_experience',
            field=models.CharField(choices=[('0', 'Fresher'), ('3', 'three months'), ('6+', 'Six months +')], default=('6+', 'Six months +'), max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.position'),
        ),
    ]
