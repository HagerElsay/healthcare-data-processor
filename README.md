# Healthcare Data Processor

A Python-based healthcare data processing prototype that extracts patient information from raw text, validates the data, de-identifies patient identifiers, and generates JSON and FHIR-style output.

## Workflow

Raw Healthcare Data
↓
Data Extraction
↓
Data Validation
↓
De-identification
↓
JSON Output
↓
FHIR-style Output

## Features

- Extracts structured data from raw patient text
- Validates required patient fields
- Detects invalid values
- De-identifies patient names
- Processes multiple patients
- Generates JSON output
- Generates FHIR-style JSON output
- Saves processed data to files

## Project Structure

```text
healthcare-data-processor/
├── main.py
├── extractor.py
├── validator.py
├── deidentifier.py
├── fhir_converter.py
├── input.txt
├── processed_patients.json
├── fhir_patients.json
└── README.md
