# Generated by Django 5.1.5 on 2025-04-11 07:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_documents_document_rename_employees_employee'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('purpose', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('requested_on', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receipt', models.FileField(upload_to='receipts/')),
                ('description', models.TextField(blank=True)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('travel_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.travelrequest')),
            ],
        ),
    ]
