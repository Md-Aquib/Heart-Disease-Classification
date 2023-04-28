from django.contrib import admin
from . models import Patient , MedicalRecord
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class PatientAdmin(ModelAdmin):
    list_display = ["first_name", "patient_id"]
    search_fields = ["first_name", "last_name", "patient_id"]
    list_filter = ["first_name", "last_name", "patient_id"]
admin.site.register(Patient, PatientAdmin)

class MedicalRecordAdmin(ModelAdmin):
    list_display = ["patient"]
    search_fields = ["patient"]
    list_filter = ["patient"]
admin.site.register(MedicalRecord, MedicalRecordAdmin)


