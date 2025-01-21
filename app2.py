import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
import pandas as pd
import io
import os

load_dotenv()

def get_pdf_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_data(text):
    llm = GoogleGenerativeAI(model="gemini-pro", temperature=0)  # Temperature 0 for consistency
    prompt_template = """
    Extract the following information from the resume text below.
    - Use the scoring criteria provided for the experience scores.
    - Return "null" for any field that does not have relevant data.
    - Extract useful data for Supporting Information

    Scoring Criteria:
    Gen AI Experience Score:
    1 – Exposed to Gen AI concepts but no practical experience.
    2 – Hands-on experience with Gen AI tools or frameworks.
    3 – Worked on advanced areas like Agentic RAG, Evals, or similar.

    AI/ML Experience Score:
    1 – Exposed to AI/ML or data science concepts but no practical experience.
    2 – Hands-on experience with AI/ML models or algorithms.
    3 – Worked on advanced AI/ML projects or systems.

    Supporting Information:
    some experience, internship, certificate,projects, research work

    Separate each key and value with "::". Do not return JSON. Just return the key-value pairs.

    Name::
    Contact Details::
    University::
    Year of Study::
    Course::
    Discipline::
    CGPA/Percentage::
    Key Skills::
    Gen AI Experience Score (1-3)::
    AI/ML Experience Score (1-3)::
    Supporting Information::

    Resume Text:
    {text}
    """
    prompt = PromptTemplate.from_template(prompt_template)
    response = llm.invoke(prompt.format(text=text))

    extracted_data = {}
    for line in response.strip().split('\n'):
        if "::" in line:
            key, value = line.split("::", 1)
            extracted_data[key.strip()] = value.strip()

    # Post-process and validate extracted values
    for score_field in ["Gen AI Experience Score (1-3)", "AI/ML Experience Score (1-3)"]:
        value = extracted_data.get(score_field, "null")
        if value not in ["1", "2", "3", "null"]:
           extracted_data[score_field] = "null"

    return extracted_data


def main():
    st.set_page_config(page_title="ATS", page_icon=":books:")
    st.header("Resume Selector")
    st.subheader("Upload your resumes")

    pdf_docs = st.file_uploader("Upload resumes", type="pdf", accept_multiple_files=True) # Accept multiple files

    if st.button("Analyze"):
        with st.spinner("Processing..."):
            if not pdf_docs:
                st.error("Please upload at least one resume.")
                return

            all_extracted_data = []
            for i, pdf_file in enumerate(pdf_docs):
                filename = os.path.basename(pdf_file.name)
                raw_text = get_pdf_text(pdf_file)
                extracted_info = extract_data(raw_text)

                extracted_info["S.No."] = i + 1
                extracted_info["Filename"] = filename
                all_extracted_data.append(extracted_info)


            # Define required fields
            required_fields = [
                "Name", "Contact Details", "University", "Year of Study", "Course",
                "Discipline", "CGPA/Percentage", "Key Skills",
                "Gen AI Experience Score (1-3)", "AI/ML Experience Score (1-3)",
                "Supporting Information"
            ]


            df = pd.DataFrame(all_extracted_data)
            df = df.reindex(columns=["S.No."] + required_fields + ["Filename"], fill_value="")

            excel_buffer = io.BytesIO()
            df.to_excel(excel_buffer, index=False, engine='openpyxl')
            excel_buffer.seek(0)

            st.download_button(
                label="Download Results",
                data=excel_buffer,
                file_name='resume_data.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

if __name__ == '__main__':
    main()