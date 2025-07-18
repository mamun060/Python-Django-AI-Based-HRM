# Generated by Django 5.1.5 on 2025-07-13 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('satisfaction', models.FloatField()),
                ('work_hours', models.IntegerField()),
                ('relationship_satisfaction', models.FloatField()),
                ('environment_satisfaction', models.FloatField()),
                ('overtime', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('education_background', models.CharField(max_length=50)),
                ('emp_department', models.CharField(max_length=50)),
                ('emp_job_role', models.CharField(max_length=50)),
                ('distance_from_home', models.FloatField()),
                ('emp_education_level', models.CharField(max_length=10)),
                ('emp_job_involvement', models.FloatField()),
                ('emp_last_salary_hike_percent', models.FloatField()),
                ('total_work_experience_in_years', models.FloatField()),
                ('predicted_churn', models.FloatField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
