from django.db import models


class StudentInfo(models.Model):

    studentID = models.IntegerField(primary_key=True, null=False)
    studentName = models.CharField(null=False)
    studentYear = models.CharField(null=False)
    courseOne = models.CharField()
    courseTwo = models.CharField()
    courseThree = models.CharField()
