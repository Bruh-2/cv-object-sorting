import cv2
import numpy as np


def segment(image):
    """
    Stage 2:
    Segment colored objects.
    """

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    color_ranges = [

        # RED
        ((0, 70, 50), (10, 255, 255)),
        ((170, 70, 50), (180, 255, 255)),

        # GREEN
        ((35, 40, 40), (90, 255, 255)),

        # BLUE
        ((90, 40, 40), (135, 255, 255)),

        # YELLOW
        ((20, 40, 40), (35, 255, 255)),

        # ORANGE
        ((10, 70, 70), (20, 255, 255)),

        # PURPLE
        ((135, 40, 40), (170, 255, 255))
    ]

    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)

    for lower, upper in color_ranges:

        lower = np.array(lower)

        upper = np.array(upper)

        current = cv2.inRange(hsv, lower, upper)

        mask = cv2.bitwise_or(mask, current)

    return mask
