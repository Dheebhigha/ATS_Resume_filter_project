import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

# Configure the API key (This line now directly sets the API key)
genai.configure(api_key=os.getenv('AIzaSyAEho69-SwcfSIy0WEWeQe0HGwsraXGJKg'))  # Using the API key from the environment variable

# Function to get Gemini response
def get_gemini_response(input):
    # Initialize the model directly here
    model = genai.GenerativeModel("gemini-1.5-flash")  # Replace with your actual model configuration
    response = model.generate_content(input)  # Generate content using the model
    return response.text

# Extract text from the PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    # Extract text from all pages in the PDF
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text 

# Prompt template
input_prompt = """
Hey Act Like a skilled or very experienced ATS(Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analysis, 
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage matching based 
on JD and the missing keywords with high accuracy.

resume: {text}
description: {jd}

I want the response in a multi-line string with a prettier structure:
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
"""

# Streamlit app
st.title("AI ATS SYSTEM")
st.text("Improve Your Resume ATS Matching")

# Input fields for job description and resume upload
jd = st.text_area("Paste the job description")
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type="pdf", help="Please upload your resume in PDF format")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        # Extract text from the uploaded PDF
        text = input_pdf_text(uploaded_file)
        
        # Format the prompt with user inputs (job description and resume text)
        prompt = input_prompt.format(jd=jd, text=text)
        
        # Get response from the Gemini model
        response = get_gemini_response(prompt)
        
        # Display the response in a readable format
        st.subheader("ATS Evaluation Result")
        st.text(response)
