# cv-object-sorting


# Automatic Color & Size Object Sorting System

## Computer Vision Team Project

This project implements a complete Computer Vision pipeline using OpenCV.

Pipeline:

Image
↓

Enhance

↓

Segment

↓

Clean

↓

Detect

↓

Decision

---

## Features

- Image enhancement using CLAHE
- HSV color segmentation
- Morphological noise removal
- Object detection using contours
- Automatic decision generation
- Saves every pipeline stage

---

## Project Structure

```
cv-object-sorting/
│
├── data/
├── output/
├── stages/
│   ├── enhance.py
│   ├── segment.py
│   ├── clean.py
│   ├── detect.py
│   └── decide.py
│
├── pipeline.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python pipeline.py
```

---

## Output

For every image the program saves:

- original.jpg
- enhanced.jpg
- mask.jpg
- clean_mask.jpg
- detection.jpg
- decision.txt

---

## Technologies

- Python
- OpenCV
- NumPy
