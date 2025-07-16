from datetime import datetime
from django.utils.timezone import localtime
from attendance.models import AttendanceRecord, DailyAttendanceSummary
from employee.models import Employee

def update_daily_summary(username):
    try:
        employee = Employee.objects.get(username=username)
    except Employee.DoesNotExist:
        return

    today = datetime.today().date()
    
    # Retrieve all records for today
    records = AttendanceRecord.objects.filter(name=username, time__date=today).order_by('time')

    if not records.exists():
        return

    # Ensure we are working with full datetime values, not just time objects
    first_record = records.first()
    last_record = records.last()

    in_time = localtime(first_record.time).time()  # in_time as time
    out_time = localtime(last_record.time).time()  # out_time as time

    # Combine the date and time parts to calculate the duration
    in_datetime = datetime.combine(today, in_time)
    out_datetime = datetime.combine(today, out_time)

    # Calculate duration (this will handle crossing midnight properly)
    duration = out_datetime - in_datetime

    # Convert total seconds to hours
    total_hours = round(duration.total_seconds() / 3600, 2)

    # Update or create the daily summary for the employee
    summary, created = DailyAttendanceSummary.objects.get_or_create(employee=employee, date=today)
    summary.in_time = in_time
    summary.out_time = out_time
    summary.total_hours = total_hours
    summary.save()

    return summary  # You can return the summary if you want to check it or log it
