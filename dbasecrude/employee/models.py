from django.db import models


class Employee(models.Model):
    Emp_id = models.IntegerField(max_length=20 , primary_key = True)
    Emp_name = models.CharField(max_length=100)
    Emp_email = models.EmailField()
    Emp_contact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"  
