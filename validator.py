def validate_patient(data):
    errors = []

    if not data.get("Patient Name"):
        errors.append("Patient Name is missing")

    if not data.get("Age"):
        errors.append("Age is missing")
    elif not data["Age"].isdigit():
        errors.append("Age must be a number")

    if data.get("Gender") not in ["Male", "Female"]:
        errors.append("Gender must be Male or Female")

    if not data.get("Diagnosis"):
        errors.append("Diagnosis is missing")

    if not data.get("Medication"):
        errors.append("Medication is missing")

    if not data.get("Blood Pressure"):
        errors.append("Blood Pressure is missing")

    return errors
