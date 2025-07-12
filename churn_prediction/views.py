import pickle
import numpy as np
import os
import pandas as pd
from django.shortcuts import render

# Django project directory থেকে BASE_DIR নিন
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the CSV data
csv_path = os.path.join(BASE_DIR, 'churn_prediction', 'Perfomance_report.csv')

df = pd.read_csv(csv_path)

# Rename columns to match the required names
df.rename(columns={
    'Satisfaction': 'SatisfactionScore',
    'Work Hours/Week': 'WorkHoursPerWeek'
}, inplace=True)

# Load the model and scaler
model = pickle.load(open(os.path.join(BASE_DIR, 'churn_prediction', 'model.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR, 'churn_prediction', 'scaler.pkl'), 'rb'))

# Select the relevant columns for prediction
df_selected = df[['Age', 'Gender', 'EducationBackground', 'EmpDepartment', 'EmpJobRole', 'DistanceFromHome', 
                  'EmpEducationLevel', 'EmpEnvironmentSatisfaction', 'WorkHoursPerWeek', 'EmpJobInvolvement', 
                  'SatisfactionScore', 'OverTime', 'EmpLastSalaryHikePercent', 'EmpRelationshipSatisfaction', 
                  'TotalWorkExperienceInYears', 'Attrition', 'PerformanceRating']]

def home(request):
    prediction = None
    kpi_info = None  # Variable to store KPI metrics for display
    employee_ids = []  # To store the matched employee IDs
    sample_data = df_selected.to_html(index=False)  # Convert selected columns to HTML table for display
    
    if request.method == 'POST':
        try:
            # Get input values from the form
            age = float(request.POST.get('age'))
            gender = request.POST.get('gender')  # Gender will be 'Male' or 'Female'
            satisfaction = float(request.POST.get('satisfaction'))
            work_hours = float(request.POST.get('work_hours'))
            overtime = request.POST.get('overtime') == 'Yes'  # 'Yes' will be 1, 'No' will be 0
            education_background = request.POST.get('education_background')  # Get Education Background
            emp_department = request.POST.get('emp_department')  # Get Employee Department
            emp_job_role = request.POST.get('emp_job_role')  # Get Employee Job Role
            distance_from_home = float(request.POST.get('distance_from_home'))
            relationship_satisfaction = float(request.POST.get('relationship_satisfaction'))
            environment_satisfaction = float(request.POST.get('environment_satisfaction'))
            emp_education_level = request.POST.get('emp_education_level')  # Get Education Level
            emp_job_involvement = float(request.POST.get('emp_job_involvement'))  # Job Involvement Score
            emp_last_salary_hike_percent = float(request.POST.get('emp_last_salary_hike_percent'))  # Last Salary Hike % 
            total_work_experience_in_years = float(request.POST.get('total_work_experience_in_years'))  # Work Experience in Years

            # Gender encoding (1 for Male, 0 for Female)
            gender_encoded = 1 if gender == 'Male' else 0

            # One-hot encode Education Background
            education_background_encoded = pd.get_dummies([education_background], 
                                                          columns=['EducationBackground'],
                                                          drop_first=True).iloc[0].to_dict()

            # Prepare input data for prediction
            input_data = pd.DataFrame({
                'Age': [age],
                'Gender': [gender_encoded],
                'SatisfactionScore': [satisfaction],
                'WorkHoursPerWeek': [work_hours],
                'OverTime': ['Yes' if overtime else 'No'],
                'EducationBackground_Marketing': [education_background_encoded.get('Marketing', 0)],
                'EducationBackground_Life Sciences': [education_background_encoded.get('Life Sciences', 0)],
                'EducationBackground_Human Resources': [education_background_encoded.get('Human Resources', 0)],
                'EducationBackground_Medical': [education_background_encoded.get('Medical', 0)],
                'EducationBackground_Other': [education_background_encoded.get('Other', 0)],
                'EducationBackground_Technical Degree': [education_background_encoded.get('Technical Degree', 0)],
                'EmpDepartment_Development': [1 if emp_department == 'Development' else 0],
                'EmpDepartment_Finance': [1 if emp_department == 'Finance' else 0],
                'EmpDepartment_Human Resources': [1 if emp_department == 'Human Resources' else 0],
                'EmpDepartment_Research & Development': [1 if emp_department == 'Research & Development' else 0],
                'EmpDepartment_Sales': [1 if emp_department == 'Sales' else 0],
                'EmpJobRole_Sales Executive': [1 if emp_job_role == 'Sales Executive' else 0],
                'EmpJobRole_Manager': [1 if emp_job_role == 'Manager' else 0],
                'EmpJobRole_Developer': [1 if emp_job_role == 'Developer' else 0],
                'EmpJobRole_Sales Representative': [1 if emp_job_role == 'Sales Representative' else 0],
                'EmpJobRole_Senior Developer': [1 if emp_job_role == 'Senior Developer' else 0],
                'EmpJobRole_Data Scientist': [1 if emp_job_role == 'Data Scientist' else 0],
                'EmpJobRole_Senior Manager R&D': [1 if emp_job_role == 'Senior Manager R&D' else 0],
                'EmpJobRole_Laboratory Technician': [1 if emp_job_role == 'Laboratory Technician' else 0],
                'EmpJobRole_Manufacturing Director': [1 if emp_job_role == 'Manufacturing Director' else 0],
                'EmpJobRole_Research Scientist': [1 if emp_job_role == 'Research Scientist' else 0],
                'EmpJobRole_Healthcare Representative': [1 if emp_job_role == 'Healthcare Representative' else 0],
                'EmpJobRole_Research Director': [1 if emp_job_role == 'Research Director' else 0],
                'EmpJobRole_Finance Manager': [1 if emp_job_role == 'Finance Manager' else 0],
                'EmpJobRole_Technical Architect': [1 if emp_job_role == 'Technical Architect' else 0],
                'EmpJobRole_Business Analyst': [1 if emp_job_role == 'Business Analyst' else 0],
                'EmpJobRole_Technical Lead': [1 if emp_job_role == 'Technical Lead' else 0],
                'EmpJobRole_Delivery Manager': [1 if emp_job_role == 'Delivery Manager' else 0],
                'DistanceFromHome': [distance_from_home],
                'EmpRelationshipSatisfaction': [relationship_satisfaction],
                'EmpEnvironmentSatisfaction': [environment_satisfaction],
                'EmpEducationLevel': [emp_education_level],
                'EmpJobInvolvement': [emp_job_involvement],
                'EmpLastSalaryHikePercent': [emp_last_salary_hike_percent],
                'TotalWorkExperienceInYears': [total_work_experience_in_years]
            })

            # One-hot encode all categorical features
            input_data_encoded = pd.get_dummies(input_data, drop_first=True)

            # Match columns with the model's expected features
            input_data_encoded = input_data_encoded.reindex(columns=model.feature_importances_, fill_value=0)

            # Scale the features using the loaded scaler
            features_scaled = scaler.transform(input_data_encoded)

            # Get the prediction from the model
            prediction_result = model.predict(features_scaled)[0]

            # Add KPI info based on input values
            kpi_info = {
                'Age': age,
                'Work_Hours_Per_Week': work_hours,
                'Satisfaction_Score': satisfaction,
                'Performance_KPI': "High" if satisfaction > 3.5 and work_hours > 40 else "Low"
            }

            # Check if input data matches the dataset for prediction
            match_found = df[(df['Age'] == age) & 
                             (df['WorkHoursPerWeek'] == work_hours) & 
                             (df['SatisfactionScore'] == satisfaction) &
                             (df['EmpRelationshipSatisfaction'] == relationship_satisfaction) & 
                             (df['EmpEnvironmentSatisfaction'] == environment_satisfaction) & 
                             (df['OverTime'] == ('Yes' if overtime else 'No'))]

            if not match_found.empty:
                # If match found, get the employee IDs and other details
                employee_ids = match_found['EmpNumber'].tolist()
                kpi_info['Employee_IDs'] = employee_ids
                kpi_info['Match_Status'] = "Employee ID match with Dataset"
            else:
                kpi_info['Match_Status'] = "Not Match the Employee ID"
                employee_ids = None

            # Determine the prediction based on Performance KPI
            if kpi_info['Performance_KPI'] == "High":
                prediction = "Stay"
            else:
                prediction = "Leave"

        except Exception as e:
            # Log the error (optional)
            print(f"Error occurred: {e}")
            # Provide a meaningful error message to the user
            prediction = f"There was an error processing your request: {e}"

    # Render the result back to the template
    return render(request, 'index.html', {
        'prediction': prediction, 
        'kpi_info': kpi_info, 
        'sample_data': sample_data
    })
