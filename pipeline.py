import os
import cv2

from stages.enhance import enhance
from stages.segment import segment
from stages.clean import clean
from stages.detect import detect
from stages.decide import decide


INPUT_FOLDER = "data"
OUTPUT_FOLDER = "output"


def process_image(image_path):

    image_name = os.path.splitext(os.path.basename(image_path))[0]

    save_folder = os.path.join(OUTPUT_FOLDER, image_name)

    os.makedirs(save_folder, exist_ok=True)

    image = cv2.imread(image_path)

    if image is None:
        print(f"Cannot open {image_path}")
        return

    # Stage 1
    enhanced = enhance(image)

    # Stage 2
    mask = segment(enhanced)

    # Stage 3
    clean_mask = clean(mask)

    # Stage 4
    detection_image, detections = detect(clean_mask, enhanced)

    # Stage 5
    decision = decide(detections)

    # Save images

    cv2.imwrite(
        os.path.join(save_folder, "original.jpg"),
        image
    )

    cv2.imwrite(
        os.path.join(save_folder, "enhanced.jpg"),
        enhanced
    )

    cv2.imwrite(
        os.path.join(save_folder, "mask.jpg"),
        mask
    )

    cv2.imwrite(
        os.path.join(save_folder, "clean_mask.jpg"),
        clean_mask
    )

    cv2.imwrite(
        os.path.join(save_folder, "detection.jpg"),
        detection_image
    )

    with open(
        os.path.join(save_folder, "decision.txt"),
        "w"
    ) as f:
        f.write(decision)

    print("--------------------------------")
    print(image_name)
    print(decision)
    print("--------------------------------")


def main():

    if not os.path.exists(INPUT_FOLDER):
        print("Folder 'data' not found.")
        return

    files = []

    for file in os.listdir(INPUT_FOLDER):

        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):
            files.append(file)

    if len(files) == 0:
        print("No images found.")
        return

    for file in files:

        process_image(
            os.path.join(INPUT_FOLDER, file)
        )

    print("\nPipeline finished successfully.")


if __name__ == "__main__":
    main()
