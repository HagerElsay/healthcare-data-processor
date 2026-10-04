def extract_patient_data(patient_text):
    data = {}

    for line in patient_text.strip().split("\n"):
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()

    return data
