# Generated by Django 3.2.8 on 2021-11-23 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0006_auto_20211122_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_awards',
            field=models.CharField(choices=[('best emp of month', 'BEOM'), ('best emp of Year', 'BEOY')], default=('best emp of month', 'BEOM'), max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.position'),
        ),
    ]
