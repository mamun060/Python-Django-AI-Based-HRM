# churn_prediction/ml_utils.py

import os
import pickle
import pandas as pd
from django.conf import settings

# Load model and scaler
MODEL_PATH = os.path.join(settings.BASE_DIR, 'churn_prediction', 'model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'churn_prediction', 'scaler.pkl')
model = pickle.load(open(MODEL_PATH, 'rb'))
scaler = pickle.load(open(SCALER_PATH, 'rb'))

def predict_from_instance(emp):
    """
    Takes an EmployeeInput instance, prepares data, and returns prediction
    """

    try:
        # Gender encoding
        gender_encoded = 1 if emp.gender == 'Male' else 0

        # One-hot encoding for job role, department, background, etc.
        input_data = {
            'Age': emp.age,
            'Gender': gender_encoded,
            'SatisfactionScore': emp.satisfaction,
            'WorkHoursPerWeek': emp.work_hours,
            'OverTime': emp.overtime,
            'EducationBackground_Marketing': 1 if emp.education_background == 'Marketing' else 0,
            'EducationBackground_Life Sciences': 1 if emp.education_background == 'Life Sciences' else 0,
            'EducationBackground_Human Resources': 1 if emp.education_background == 'Human Resources' else 0,
            'EducationBackground_Medical': 1 if emp.education_background == 'Medical' else 0,
            'EducationBackground_Other': 1 if emp.education_background == 'Other' else 0,
            'EducationBackground_Technical Degree': 1 if emp.education_background == 'Technical Degree' else 0,
            'EmpDepartment_Development': 1 if emp.emp_department == 'Development' else 0,
            'EmpDepartment_Finance': 1 if emp.emp_department == 'Finance' else 0,
            'EmpDepartment_Human Resources': 1 if emp.emp_department == 'Human Resources' else 0,
            'EmpDepartment_Research & Development': 1 if emp.emp_department == 'Research & Development' else 0,
            'EmpDepartment_Sales': 1 if emp.emp_department == 'Sales' else 0,
            'EmpJobRole_Sales Executive': 1 if emp.emp_job_role == 'Sales Executive' else 0,
            'EmpJobRole_Manager': 1 if emp.emp_job_role == 'Manager' else 0,
            'EmpJobRole_Developer': 1 if emp.emp_job_role == 'Developer' else 0,
            'EmpJobRole_Senior Developer': 1 if emp.emp_job_role == 'Senior Developer' else 0,
            'EmpJobRole_Data Scientist': 1 if emp.emp_job_role == 'Data Scientist' else 0,
            'EmpJobRole_Laboratory Technician': 1 if emp.emp_job_role == 'Laboratory Technician' else 0,
            'EmpJobRole_Research Scientist': 1 if emp.emp_job_role == 'Research Scientist' else 0,
            'EmpJobRole_Senior Manager R&D': 1 if emp.emp_job_role == 'Senior Manager R&D' else 0,
            'EmpJobRole_Research Director': 1 if emp.emp_job_role == 'Research Director' else 0,
            'EmpJobRole_Healthcare Representative': 1 if emp.emp_job_role == 'Healthcare Representative' else 0,
            'EmpJobRole_Finance Manager': 1 if emp.emp_job_role == 'Finance Manager' else 0,
            'EmpJobRole_Technical Architect': 1 if emp.emp_job_role == 'Technical Architect' else 0,
            'EmpJobRole_Technical Lead': 1 if emp.emp_job_role == 'Technical Lead' else 0,
            'EmpJobRole_Business Analyst': 1 if emp.emp_job_role == 'Business Analyst' else 0,
            'EmpJobRole_Delivery Manager': 1 if emp.emp_job_role == 'Delivery Manager' else 0,
            'DistanceFromHome': emp.distance_from_home,
            'EmpRelationshipSatisfaction': emp.relationship_satisfaction,
            'EmpEnvironmentSatisfaction': emp.environment_satisfaction,
            'EmpEducationLevel': emp.emp_education_level,
            'EmpJobInvolvement': emp.emp_job_involvement,
            'EmpLastSalaryHikePercent': emp.emp_last_salary_hike_percent,
            'TotalWorkExperienceInYears': emp.total_work_experience_in_years
        }

        df = pd.DataFrame([input_data])
        df = df.reindex(columns=scaler.get_feature_names_out(), fill_value=0)
        scaled = scaler.transform(df)
        prediction = model.predict(scaled)[0]
        return prediction

    except Exception as e:
        print(f"Prediction error for {emp.id}: {e}")
        return None
