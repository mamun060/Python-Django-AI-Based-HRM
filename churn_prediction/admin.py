from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import EmployeeInput
from .forms import EmployeeInputForm
from .predict import predict_employee_status  # your custom prediction function
from app.models import Employee
import pickle
import pandas as pd
from django.conf import settings
import os

# Load model and scaler once
MODEL_PATH = os.path.join(settings.BASE_DIR, 'churn_prediction', 'model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'churn_prediction', 'scaler.pkl')
model = pickle.load(open(MODEL_PATH, 'rb'))
scaler = pickle.load(open(SCALER_PATH, 'rb'))

@admin.action(description='Predict Churn')
def predict_churn(modeladmin, request, queryset):
    for obj in queryset:
        try:
            df = pd.DataFrame([{
                'Age': obj.age,
                'Gender': 1 if obj.gender == 'Male' else 0,
                'SatisfactionScore': obj.satisfaction,
                'WorkHoursPerWeek': obj.work_hours,
                'OverTime': obj.overtime,
                'EducationBackground_Marketing': 1 if obj.education_background == 'Marketing' else 0,
                'EducationBackground_Life Sciences': 1 if obj.education_background == 'Life Sciences' else 0,
                'EducationBackground_Human Resources': 1 if obj.education_background == 'Human Resources' else 0,
                'EducationBackground_Medical': 1 if obj.education_background == 'Medical' else 0,
                'EducationBackground_Other': 1 if obj.education_background == 'Other' else 0,
                'EducationBackground_Technical Degree': 1 if obj.education_background == 'Technical Degree' else 0,
                'EmpDepartment_Development': 1 if obj.emp_department == 'Development' else 0,
                'EmpDepartment_Finance': 1 if obj.emp_department == 'Finance' else 0,
                'EmpDepartment_Human Resources': 1 if obj.emp_department == 'Human Resources' else 0,
                'EmpDepartment_Research & Development': 1 if obj.emp_department == 'Research & Development' else 0,
                'EmpDepartment_Sales': 1 if obj.emp_department == 'Sales' else 0,
                'EmpJobRole_' + obj.emp_job_role: 1,
                'DistanceFromHome': obj.distance_from_home,
                'EmpRelationshipSatisfaction': obj.relationship_satisfaction,
                'EmpEnvironmentSatisfaction': obj.environment_satisfaction,
                'EmpEducationLevel': obj.emp_education_level,
                'EmpJobInvolvement': obj.emp_job_involvement,
                'EmpLastSalaryHikePercent': obj.emp_last_salary_hike_percent,
                'TotalWorkExperienceInYears': obj.total_work_experience_in_years
            }])

            # Fill missing columns if any
            df = df.reindex(columns=scaler.get_feature_names_out(), fill_value=0)

            scaled = scaler.transform(df)
            prediction = model.predict(scaled)[0]

            obj.predicted_churn = prediction
            obj.save()

        except Exception as e:
            print(f"Prediction failed for {obj.id}: {e}")

class EmployeeInputAdmin(ModelAdmin):
    list_display = ('id', 'employee_name', 'employee_role', 'age', 'gender', 'emp_job_role', 'satisfaction', 'predicted_churn')
    list_filter = ('gender', 'emp_department', 'emp_job_role', 'overtime')
    search_fields = ('employee__name', 'employee__role', 'emp_job_role')
    actions = [predict_churn]
    def employee_name(self, obj):
        return obj.employee.name

    def employee_role(self, obj):
        return obj.employee.designation

    employee_name.short_description = 'Employee Name'
    employee_role.short_description = 'Employee designation'

    fieldsets = (
        ('Basic Info', {
            'fields':  (
            ('employee', 'age'),
            ('gender', 'emp_job_role'),
            ('emp_department',),
        ),
            'classes': ('unfold',),
        }),
        ('Job Satisfaction', {
            'fields': (
                ('satisfaction', 'work_hours'),
                ('relationship_satisfaction', 'environment_satisfaction'),
            ),
            'classes': ('unfold',),
        }),
        ('Additional Details', {
            'fields': (
                (
                    'overtime', 'education_background'
                ),
                (
                    'distance_from_home', 'emp_education_level'
                ),
                (
                    'emp_job_involvement', 'emp_last_salary_hike_percent', 'total_work_experience_in_years'
                ),
                # (
                #     'predicted_churn'
                # )
            ),
            'classes': ('unfold',),
        }),
    )

    # readonly_fields = ('predicted_churn',)

    def save_model(self, request, obj, form, change):
        # Assuming you have a predict_employee_status function defined elsewhere
        obj.predicted_churn = predict_employee_status(obj)
        super().save_model(request, obj, form, change)

admin.site.register(EmployeeInput, EmployeeInputAdmin)