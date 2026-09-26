import argparse
import os

from src.pipeline import recognize_license_plate


def main():
    parser = argparse.ArgumentParser(
        description="License Plate Recognition using OpenCV and EasyOCR"
    )
    parser.add_argument(
        "--image",
        required=True,
        help="Path to the input vehicle image"
    )
    parser.add_argument(
        "--output",
        default="images/output/result.jpg",
        help="Path for the processed output image"
    )

    args = parser.parse_args()

    if not os.path.isfile(args.image):
        raise FileNotFoundError(f"Input image not found: {args.image}")

    result = recognize_license_plate(args.image, args.output)

    print("\n--- License Plate Recognition Result ---")
    print(f"Detected text: {result['text'] or 'Not confidently recognized'}")
    print(f"Confidence: {result['confidence']:.2f}")
    print(f"Candidates checked: {result['candidates_checked']}")
    print(f"Output image: {result['output_path']}")


if __name__ == "__main__":
    main()
