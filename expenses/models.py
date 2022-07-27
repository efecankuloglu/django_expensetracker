from django.db import models


class ExpenseRecord(models.Model):
    choices = [
        ('In', "In"),
        ('Out', "Out"),
    ]

    date = models.DateField()
    location = models.CharField(max_length=20)
    bill_no = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    in_out = models.CharField('In/Out', choices=choices, max_length=5)
    amount = models.FloatField()
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.date) + " " + self.description
