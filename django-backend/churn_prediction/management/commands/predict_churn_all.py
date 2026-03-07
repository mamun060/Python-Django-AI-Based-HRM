# churn_prediction/management/commands/predict_churn_all.py

from django.core.management.base import BaseCommand
from churn_prediction.models import EmployeeInput
from churn_prediction.ml_utils import predict_from_instance

class Command(BaseCommand):
    help = 'Run churn prediction on all EmployeeInput records and save results.'

    def handle(self, *args, **kwargs):
        employees = EmployeeInput.objects.all()
        for emp in employees:
            prediction = predict_from_instance(emp)
            if prediction is not None:
                emp.predicted_churn = prediction
                emp.save()
                self.stdout.write(self.style.SUCCESS(f'Updated {emp.id} with churn: {prediction}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed prediction for {emp.id}'))
