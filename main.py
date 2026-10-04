import json

from extractor import extract_patient_data
from validator import validate_patient
from deidentifier import deidentify_patient
from fhir_converter import convert_to_fhir


print("Healthcare Data Processor")
print("-------------------------")


with open("input.txt", "r") as file:
    input_data = file.read()


patients = input_data.strip().split("\n\n")

processed_patients = []
fhir_patients = []


for index, patient_text in enumerate(patients, start=1):

    data = extract_patient_data(patient_text)

    errors = validate_patient(data)

    if errors:
        print("\nInvalid patient:")
        for error in errors:
            print("-", error)
        continue

    data = deidentify_patient(data)

    processed_patients.append(data)

    fhir_patient = convert_to_fhir(data, index)
    fhir_patients.append(fhir_patient)


json_output = json.dumps(processed_patients, indent=4)

with open("processed_patients.json", "w") as file:
    file.write(json_output)


fhir_output = json.dumps(fhir_patients, indent=4)

with open("fhir_patients.json", "w") as file:
    file.write(fhir_output)


print("\nProcessed Patients:")
print(json_output)

print("\nFHIR Output:")
print(fhir_output)

print("\nFiles saved successfully:")
print("- processed_patients.json")
print("- fhir_patients.json")
