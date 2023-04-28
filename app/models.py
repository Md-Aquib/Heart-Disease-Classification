from django.db import models
from django.db.models.deletion import CASCADE
import datetime

# Create your models here.

def incre_patient_id():
    last_patient = Patient.objects.all().order_by('id').last()
    if not last_patient:
        return str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '0000'
    patient_id = last_patient.patient_id
    patient_int = int(patient_id[6:13])
    new_patient_int = patient_int + 123
    new_patient_id = 'RNH' + str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + str(new_patient_int).zfill(4)
    return new_patient_id


class Patient(models.Model):
    first_name = models.CharField(max_length = 20,default="first_name")
    last_name = models.CharField(max_length = 30,default="last_name")
    patient_id = models.CharField(max_length = 20,default=incre_patient_id, editable=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=30,default="Male",choices=(("Male","Male"),("Female","Female")))

    def __str__(self):
        return "%s" % self.patient_id

class MedicalRecord(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=CASCADE)
    cp = models.IntegerField(default=0,choices=((0,0),(1,1),(2,2),(3,3)))
    bp = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField(default=0,choices=((0,0),(1,1)))
    restecg = models.IntegerField(default=0,choices=((0,0),(1,1),(2,2)))
    thalach = models.IntegerField()
    exang = models.IntegerField(default=0,choices=((0,0),(1,1)))
    oldpeak = models.FloatField()
    slope = models.IntegerField(default=0,choices=((0,0),(1,1),(2,2)))
    ca = models.IntegerField()
    thal = models.IntegerField()
    result = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.patient