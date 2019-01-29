from django.db import models
import uuid


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField()

    def __str__(self):
        return str(self.employee_id)


class Device(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device_id = models.CharField(default=uuid.uuid4(), max_length=50)

    def __str__(self):
        return self.device_id
