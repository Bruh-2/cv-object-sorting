import os
import cv2

from stages.enhance import enhance
from stages.segment import segment
from stages.clean import clean
from stages.detect import detect
from stages.decide import decide

INPUT_FOLDER = "data"
OUTPUT_FOLDER = "output"


def save_image(path, image):
    """
    Save image to disk.
    """
    cv2.imwrite(path, image)


def process_image(image_path):
    """
    Process one image through the complete CV pipeline.
    """

    image_name = os.path.splitext(os.path.basename(image_path))[0]

    print(f"\nProcessing: {image_name}")

    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Cannot read {image_path}")
        return False

    output_dir = os.path.join(OUTPUT_FOLDER, image_name)
    os.makedirs(output_dir, exist_ok=True)

    # ==========================
    # Stage 1 - Enhance
    # ==========================

    enhanced = enhance(image)

    # ==========================
    # Stage 2 - Segment
    # ==========================

    mask = segment(enhanced)

    # ==========================
    # Stage 3 - Clean
    # ==========================

    cleaned = clean(mask)

    # ==========================
    # Stage 4 - Detect
    # ==========================

    detection_image, detections = detect(cleaned, enhanced)

    # ==========================
    # Stage 5 - Decision
    # ==========================

    report = decide(detections)

    # ==========================
    # Save Results
    # ==========================

    save_image(os.path.join(output_dir, "original.jpg"), image)
    save_image(os.path.join(output_dir, "enhanced.jpg"), enhanced)
    save_image(os.path.join(output_dir, "mask.jpg"), mask)
    save_image(os.path.join(output_dir, "clean_mask.jpg"), cleaned)
    save_image(os.path.join(output_dir, "detection.jpg"), detection_image)

    report_path = os.path.join(output_dir, "decision.txt")

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

    print("✓ Enhancement completed")
    print("✓ Segmentation completed")
    print("✓ Cleaning completed")
    print("✓ Detection completed")
    print("✓ Decision completed")

    print(f"Objects detected: {len(detections)}")

    print(f"Results saved to: {output_dir}")

    return True


def main():

    print("=" * 50)
    print("Computer Vision Object Sorting System")
    print("=" * 50)

    if not os.path.exists(INPUT_FOLDER):
        print(f"Folder '{INPUT_FOLDER}' does not exist.")
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    image_files = []

    for file in os.listdir(INPUT_FOLDER):

        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            image_files.append(file)

    if len(image_files) == 0:
        print("No images found in data folder.")
        return

    print(f"\nFound {len(image_files)} image(s).")

    success = 0

    for image_file in image_files:

        image_path = os.path.join(INPUT_FOLDER, image_file)

        if process_image(image_path):
            success += 1

    print("\n" + "=" * 50)
    print("Pipeline Finished")
    print("=" * 50)

    print(f"Processed images: {success}/{len(image_files)}")
    print(f"Results folder: {OUTPUT_FOLDER}")


if __name__ == "__main__":
    main()
