def deidentify_patient(data):
    data["Patient Name"] = "[DE-IDENTIFIED]"
    return data
