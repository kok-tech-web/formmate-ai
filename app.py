import streamlit as st
import pytesseract
from PIL import Image
import pdfplumber

st.set_page_config(page_title="FormMate AI", layout="centered")

st.title("📄 FormMate AI")
st.write("Upload a scanned image or PDF file to extract and view its text content instantly.")

uploaded_file = st.file_uploader("Upload a file", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    with st.spinner("Processing..."):

        if uploaded_file.type == "application/pdf":
            text = ""
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        else:
            image = Image.open(uploaded_file)
            text = pytesseract.image_to_string(image)

    st.success("Extraction complete! 🎉")
    st.subheader("📝 Extracted Text")
    st.text_area("Result", text, height=300)
