# cv-object-sorting


# Automatic Object Sorting System

## Computer Vision Course Project

This project implements a complete **Computer Vision pipeline** for automatic object detection and sorting based on **color** and **size**.

The system processes input images automatically and saves the result of every processing stage.

---

# Pipeline

| Stage | Description | Key Methods |
|------|-------------|-------------|
| **Enhance** | Improves image quality before processing | Gaussian Blur, CLAHE |
| **Segment** | Segments colored objects using HSV color space | HSV Conversion, Color Thresholding |
| **Clean** | Removes noise from the binary mask | Morphological Opening, Dilation |
| **Detect** | Detects object contours and classifies each object | Contour Detection, Bounding Boxes, Color Classification |
| **Decide** | Generates the final automatic report | Object Counting, Size Classification, Decision Generation |

---

# Project Structure

```text
cv-object-sorting/
│
├── data/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── image3.jpg
│
├── output/
│
├── report/
│
├── stages/
│   ├── enhance.py
│   ├── segment.py
│   ├── clean.py
│   ├── detect.py
│   └── decide.py
│
├── pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Processing Workflow

```
Input Image
      │
      ▼
 Enhance
      │
      ▼
 Segment
      │
      ▼
  Clean
      │
      ▼
 Detect
      │
      ▼
 Decide
      │
      ▼
 Final Report
```

---

# Supported Colors

The system can classify the following object colors:

- 🔴 Red
- 🟢 Green
- 🔵 Blue
- 🟡 Yellow
- 🟠 Orange
- 🟣 Purple

---

# Object Classification

For every detected object the system determines:

- Color
- Size (Small / Large)
- Position
- Bounding Box

---

# Output

For every processed image the program saves:

```text
output/

image/

original.jpg

enhanced.jpg

mask.jpg

clean_mask.jpg

detection.jpg

decision.txt
```

---

# Technologies

- Python 3
- OpenCV
- NumPy
- Matplotlib

---

# Installation

```bash
pip install -r requirements.txt
```

---

# Run

```bash
python pipeline.py
```

---

# Example Output

The program automatically:

- Enhances the input image
- Segments colored objects
- Removes image noise
- Detects object contours
- Classifies objects by color and size
- Generates an automatic report

---

# Authors

Computer Vision Course Project

2025
