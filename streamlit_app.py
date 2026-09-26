import os
import sys
import tempfile

import streamlit as st
from PIL import Image

# Allow imports from the project root.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.pipeline import recognize_license_plate


st.set_page_config(
    page_title="License Plate Recognition",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 License Plate Recognition System")
st.write(
    "Upload a vehicle image to detect a possible license plate "
    "and recognize its text using OpenCV and EasyOCR."
)

uploaded_file = st.file_uploader(
    "Upload a vehicle image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Input Image")
    st.image(image, use_container_width=True)

    if st.button("Recognize License Plate", type="primary"):
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        ) as temp_file:
            image.save(temp_file.name)
            input_path = temp_file.name

        output_path = os.path.join(
            ROOT,
            "images",
            "output",
            "streamlit_result.jpg"
        )

        with st.spinner("Detecting and reading the license plate..."):
            try:
                result = recognize_license_plate(
                    input_path,
                    output_path
                )

                st.subheader("Result")

                if result["text"]:
                    st.success(
                        f"Detected Plate: {result['text']}"
                    )
                    st.write(
                        f"Confidence: {result['confidence']:.2f}"
                    )
                else:
                    st.warning(
                        "A plate region may have been found, "
                        "but the text could not be confidently recognized."
                    )

                if os.path.exists(output_path):
                    st.image(
                        output_path,
                        caption="Processed Image",
                        use_container_width=True
                    )

            except Exception as exc:
                st.error(f"Processing failed: {exc}")

            finally:
                if os.path.exists(input_path):
                    os.remove(input_path)
