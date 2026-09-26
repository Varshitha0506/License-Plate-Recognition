# License Plate Recognition System

A Python-based License Plate Recognition (LPR) system that detects possible vehicle license-plate regions using OpenCV and extracts plate text using EasyOCR.

## Project Objective

The goal of this project is to automate license-plate detection and text recognition from vehicle images.

## Features

- Upload a vehicle image
- Detect possible license-plate regions using OpenCV
- Preprocess the detected plate for OCR
- Extract alphanumeric text using EasyOCR
- Draw the detected plate region on the image
- Save the processed result
- Streamlit web interface
- Command-line execution
- Modular and easy-to-extend structure

## Tech Stack

- Python 3.9+
- OpenCV
- EasyOCR
- NumPy
- Pillow
- Streamlit

## Architecture

```text
Input Image
    |
    v
Image Preprocessing
    |
    v
Edge Detection
    |
    v
Contour Detection
    |
    v
Plate Candidate Filtering
    |
    v
Plate Preprocessing
    |
    v
EasyOCR
    |
    v
Recognized Plate Number
    |
    v
Output Image
```

## Folder Structure

```text
License-Plate-Recognition-System/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── __init__.py
│   ├── detector.py
│   ├── ocr.py
│   └── pipeline.py
│
├── utils/
│   ├── __init__.py
│   ├── image_utils.py
│   └── text_utils.py
│
├── images/
│   ├── input/
│   └── output/
│
├── models/
│   └── README.md
│
├── docs/
│   └── PROJECT_NOTES.md
│
├── tests/
│   └── test_text_utils.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run from Command Line

Place a vehicle image in:

```text
images/input/
```

Then run:

```bash
python main.py --image images/input/sample.jpg
```

The result is saved in:

```text
images/output/
```

## Run the Web Application

```bash
streamlit run app/streamlit_app.py
```

Then open the local Streamlit URL shown in the terminal.

## Important Notes

OCR accuracy depends on:
- image resolution
- lighting
- camera angle
- plate visibility
- image quality
- vehicle/plate format

This project uses OpenCV contour-based candidate detection and EasyOCR. It does not include a trained YOLOv8 model by default. A YOLOv8 detector can be integrated later by adding trained weights to the `models/` directory.

## Future Enhancements

- YOLOv8-based license-plate detection
- Real-time webcam recognition
- Video processing
- Multi-vehicle detection
- Database storage
- Flask/FastAPI REST API
- Indian number-plate specific validation
- Deployment to a cloud platform
