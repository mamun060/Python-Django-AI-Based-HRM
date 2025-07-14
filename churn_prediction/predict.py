def predict_employee_status(obj):
    score = obj.satisfaction * 0.4 + obj.emp_job_involvement * 0.6
    if obj.overtime == 'Yes':
        score += 0.3
    return round(score, 2)
