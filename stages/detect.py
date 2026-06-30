import cv2


def detect(mask, image):
    """
    Stage 4:
    Detect objects using contours.

    Returns:
        image_with_boxes
        detections
    """

    output = image.copy()

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    detections = []

    object_id = 1

    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore tiny objects
        if area < 300:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        cx = x + w // 2
        cy = y + h // 2

        detections.append({
            "id": object_id,
            "x": x,
            "y": y,
            "width": w,
            "height": h,
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

        # Draw center point
        cv2.circle(
            output,
            (cx, cy),
            4,
            (0, 0, 255),
            -1
        )

        # Draw ID
        cv2.putText(
            output,
            f"ID {object_id}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

        object_id += 1

    return output, detections
