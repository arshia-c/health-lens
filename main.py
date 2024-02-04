
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
from api_key import api_key


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app



st.header("Health Lens 🔍")

st.subheader("")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

input=st.text_input("Input Prompt: ",key="input")

pro="""
  Analyze the given medical image and describe its visual characteristics. This includes as side heading:

Modality: What type of image is it? (e.g., X-ray, MRI, CT scan)
Anatomy: What anatomical structures are visible in the image? (e.g., bones, muscles, organs)
Key features: Identify any prominent features or abnormalities in the image. (e.g., fractures, lesions, tumors)
Spatial relationships: Describe the positions and relationships between different structures. (e.g., organ displacement, tissue density variations)

Additional notes:

Be specific about the types of medical images your application will support.
Clearly state that the output is a description of visual features, not a medical diagnosis.
Emphasize the importance of seeking professional medical advice for any health concerns.

"""


submit=st.button("Generate Analysis")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(pro,image)
    st.subheader("The Response is")
    st.write(response)
    st.write("This system prompt is for informative purposes only, and the development and deployment of any actual system should comply with ethical guidelines, privacy regulations, and professional standards in the field of medicine")