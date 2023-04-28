from django.shortcuts import render
from . models import Patient, MedicalRecord
import pickle
import numpy as np

# Create your views here.

def UID(request):
    if request.method == 'POST':
        uid = request.POST['uid']

        patient_details = Patient.objects.get(patient_id=uid)

        global details

        details = {'id': patient_details.patient_id,
                   'first_name':patient_details.first_name,
                   'last_name':patient_details.last_name,
                   'age':patient_details.age,
                   'gender':patient_details.gender}

        return render(request,'base.html', details)

    return render(request,'uid.html')

def Home(request):
    if request.method == "POST":
        cp = request.POST['cp']
        bp = request.POST['bp']
        chol = request.POST['chol']
        fbs = request.POST['pt_fbs']
        restecg = request.POST['restecg']
        thalach = request.POST['thalach']
        exang = request.POST['exang']
        oldpeak = request.POST['oldpeak']
        slope = request.POST['slope']
        ca = request.POST['ca']
        thal = request.POST['thal']

        if details['gender'] == 'Male':
            gender = 1
        else:
            gender = 0

        features = [int(details['age']), gender , int(cp), int(bp), int(chol),
                    int(fbs), int(restecg), int(thalach), int(exang),
                    float(oldpeak), int(slope), int(ca), int(thal)]

        data = np.array([features])
        file = open(r'heartdisease.pkl','rb')
        model = pickle.load(file)
        result = model.predict(data)

        patient_dt = Patient.objects.get(patient_id = int(details['id']))

        medical = MedicalRecord(patient= patient_dt,
                                cp = int(cp),
                                bp = int(bp),
                                chol = int(chol),
                                fbs = int(fbs),
                                restecg = int(restecg),
                                thalach = int(thalach),
                                exang = int(exang),
                                oldpeak = float(oldpeak),
                                slope = int(slope),
                                ca = int(ca),
                                thal = int(thal),
                                result = int(result))

        medical.save()

        return render(request, 'result.html', {'result': result[0]})

    return render(request,'base.html')

def result(request):
    result = 0
    return render(request, 'result.html', {'result': result})