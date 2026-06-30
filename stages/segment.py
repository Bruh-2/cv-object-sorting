import cv2
import numpy as np


def segment(image):
    """
    Stage 2: Segment colored objects using HSV.

    Returns:
        binary mask
    """

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # ----- RED -----

    lower_red1 = np.array([0, 80, 80])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 80, 80])
    upper_red2 = np.array([180, 255, 255])

    red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    red2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = red1 + red2

    # ----- GREEN -----

    lower_green = np.array([35, 60, 60])
    upper_green = np.array([90, 255, 255])

    green_mask = cv2.inRange(
        hsv,
        lower_green,
        upper_green
    )

    # ----- BLUE -----

    lower_blue = np.array([95, 80, 80])
    upper_blue = np.array([135, 255, 255])

    blue_mask = cv2.inRange(
        hsv,
        lower_blue,
        upper_blue
    )

    # Combine masks

    mask = red_mask | green_mask | blue_mask

    return mask
