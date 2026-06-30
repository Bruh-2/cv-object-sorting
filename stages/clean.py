import cv2
import numpy as np


def clean(mask):
    """
    Stage 3: Remove noise from segmentation mask.

    Returns:
        cleaned binary mask
    """

    kernel = np.ones((5, 5), np.uint8)

    # Remove small noise
    cleaned = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    # Fill small holes
    cleaned = cv2.morphologyEx(
        cleaned,
        cv2.MORPH_CLOSE,
        kernel
    )

    return cleaned
