def decide(detections):
    """
    Stage 5:
    Make the final decision based on detected objects.

    Returns:
        decision_text
    """

    total_objects = len(detections)

    small_objects = 0
    large_objects = 0

    AREA_THRESHOLD = 5000

    for obj in detections:
        if obj["area"] < AREA_THRESHOLD:
            small_objects += 1
        else:
            large_objects += 1

    decision = []

    decision.append("===== OBJECT SORTING REPORT =====")
    decision.append(f"Total objects detected: {total_objects}")
    decision.append(f"Small objects: {small_objects}")
    decision.append(f"Large objects: {large_objects}")
    decision.append("")

    if total_objects == 0:
        decision.append("Decision: No objects detected.")
    else:
        decision.append("Decision: Object sorting completed successfully.")

    return "\n".join(decision)
