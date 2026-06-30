import cv2


def enhance(image):
    """
    Stage 1: Enhance image quality.

    Steps:
    - Gaussian Blur (noise reduction)
    - CLAHE (contrast enhancement)

    Returns:
        enhanced image
    """

     
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

     
    lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

    l, a, b = cv2.split(lab)

     
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    l = clahe.apply(l)

    enhanced = cv2.merge((l, a, b))

    enhanced = cv2.cvtColor(
        enhanced,
        cv2.COLOR_LAB2BGR
    )

    return enhanced
