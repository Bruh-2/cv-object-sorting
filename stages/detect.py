import cv2
import numpy as np


def get_color(hsv_pixel):
    """
    Detect object color from HSV pixel.
    """

    h, s, v = hsv_pixel

    # Red
    if (h <= 10 or h >= 170) and s > 60:
        return "Red"

    # Green
    elif 35 <= h <= 90:
        return "Green"

    # Blue
    elif 95 <= h <= 135:
        return "Blue"

    return "Unknown"


def detect(mask, image):
    """
    Stage 4:
    Detect objects and classify by color and size.
    """

    output = image.copy()

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    detections = []

    object_id = 1

    for contour in contours:

        area = cv2.contourArea(contour)

        if area < 300:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        cx = x + w // 2
        cy = y + h // 2

        color = get_color(hsv[cy, cx])

        size = "Large" if area >= 5000 else "Small"

        detections.append({
            "id": object_id,
            "color": color,
            "size": size,
            "area": area,
            "center": (cx, cy)
        })

        # Draw rectangle
        cv2.rectangle(
            output,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Draw label
        label = f"{color} | {size}"

        cv2.putText(
            output,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2
        )

        object_id += 1

    return output, detections
