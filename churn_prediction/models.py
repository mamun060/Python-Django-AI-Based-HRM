import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

# Load the CSV data
df = pd.read_csv('Perfomance_report.csv')  # Path to your dataset

# প্রয়োজনীয় কলাম নির্বাচন
df_selected = df[['Age', 'Gender', 'EducationBackground', 'EmpDepartment', 'EmpJobRole', 'DistanceFromHome',
                  'EmpEducationLevel', 'EmpEnvironmentSatisfaction', 'WorkHoursPerWeek', 'EmpJobInvolvement', 'SatisfactionScore', 
                  'OverTime', 'EmpLastSalaryHikePercent', 'EmpRelationshipSatisfaction', 'TotalWorkExperienceInYears', 'Attrition', 
                  'PerformanceRating']]

# ফিচার এবং লেবেল সিলেকশন
X = df_selected.drop(columns=['Attrition'])  # ফিচারগুলো
y = df_selected['Attrition']  # লেবেল

# ক্যাটেগোরিকাল ফিচারগুলো এনকোড করা
X = pd.get_dummies(X, drop_first=True)

# ডেটা স্কেলিং
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ডেটা ট্রেনিং এবং টেস্টিং সেটে ভাগ করা
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# মডেল ট্রেনিং
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# মডেল পরীক্ষণ
y_pred = model.predict(X_test)

# অ্যাকিউরেসি চেক করা
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# ক্লাসিফিকেশন রিপোর্ট
print(classification_report(y_test, y_pred))

# মডেল এবং স্কেলার সেভ করা
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('scaling.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)