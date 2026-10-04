def convert_to_fhir(data, patient_id):
    return {
        "resourceType": "Patient",
        "id": str(patient_id),
        "gender": data["Gender"].lower(),
        "age": data["Age"],
        "diagnosis": data["Diagnosis"],
        "medication": data["Medication"],
        "bloodPressure": data["Blood Pressure"]
    }
