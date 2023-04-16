from django.db import models

# class Calculator(models.Model):
#     a = models.FloatField(help_text="first operand")
#     b = models.FloatField(help_text="second operand")
#     op = models.CharField(max_length=10)

class CalcResult():
    a = models.IntegerField(help_text="second operand")
    b = models.IntegerField(help_text="second operand")
    op = models.CharField(max_length=1)
    result = models.IntegerField(help_text="result")