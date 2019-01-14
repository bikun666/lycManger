from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employeeNo = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    password = models.CharField(default="", max_length=16)
    authority = models.IntegerField(default="0")

    class Meta:
        db_table = 'employee'
        verbose_name = "社員表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
