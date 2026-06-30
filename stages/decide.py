def decide(detections):
    """
    Stage 5:
    Generate final report.
    """

    total = len(detections)

    red = 0
    green = 0
    blue = 0

    small = 0
    large = 0

    report = []

    report.append("===== OBJECT SORTING REPORT =====")
    report.append("")

    for obj in detections:

        report.append(
            f"Object {obj['id']}: {obj['color']} | {obj['size']}"
        )

        if obj["color"] == "Red":
            red += 1

        elif obj["color"] == "Green":
            green += 1

        elif obj["color"] == "Blue":
            blue += 1

        if obj["size"] == "Small":
            small += 1
        else:
            large += 1

    report.append("")
    report.append("----------------------------")
    report.append(f"Total objects : {total}")
    report.append("")
    report.append(f"Red objects   : {red}")
    report.append(f"Green objects : {green}")
    report.append(f"Blue objects  : {blue}")
    report.append("")
    report.append(f"Small objects : {small}")
    report.append(f"Large objects : {large}")
    report.append("")

    if total == 0:
        report.append("Decision: No objects detected.")
    else:
        report.append("Decision: Object sorting completed successfully.")

    return "\n".join(report)
