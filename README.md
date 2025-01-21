# ATS_LLM
This is an ATS using LLM to test out the capabilities of Generative AI. This project is a Streamlit-based application designed to efficiently extract key information from resumes and output the results to an organized Excel file. This tool is particularly useful for recruiters and hiring managers looking to quickly process a large number of resumes.


![image](https://github.com/user-attachments/assets/89b13e1d-1645-47fc-8bc3-a8581f87767a)



## This project aims to showcase proficiency in several key areas:

*   **Speed:** Efficient processing of resumes.
*   **Quality:** Accuracy and completeness of extracted data.
*   **Accuracy:** Precise extraction of data into mandatory columns.
*   **Creativity:** Innovative use of Generative AI and insightful output.

## Features

1.  **Generative AI Integration:**
    *   Utilizes the **Google Gemini Pro** model for text extraction.
    *   Employs a well-defined prompt to guide the LLM in extracting specific fields and generating scores with limited context.

2.  **Accurate Data Extraction:**
    *   Extracts the following fields: Name, Contact Details, University, Year of Study, Course, Discipline, CGPA/Percentage, Key Skills, Gen AI Experience Score (1-3), AI/ML Experience Score (1-3), Supporting Information, and Interesting Information.
    *   Handles varied resume formats and layouts effectively, using explicit instructions in the prompt to manage different patterns in data representation.
    *   Includes post-processing steps to ensure all values are accurate and within the expected range or marked as `null`.

3.  **Scoring Mechanism:**
    *   Provides a structured scoring mechanism for Gen AI and AI/ML experience using a 1-3 scale with clearly defined levels (Exposed, Hands-on, Advanced).

4.  **Simplicity:**
    *   A simplified prompting approach, avoiding complex logic, and using direct extraction makes the LLM inference much faster.
    *   The project is built in a way that the individual extraction and scoring logic is efficient and can scale with more resumes.

5.  **Creativity and Innovation:**
    *   **"Interesting Information" field:** Captures any unique or noteworthy information from the resume, like hobbies, projects, or research, adding a qualitative insight. This feature is intended to capture anything interesting that might otherwise be overlooked by more rigid, field-specific extraction processes.
    *   **Post-processing validation:**  The code uses a validation step to ensure that experience scores are within the valid 1-3 range and correctly labels missing information as `null`, which makes it more robust.

7.  **Output Quality:**
    *   The results are outputted into a neatly formatted Excel file with proper headings, making the data easy to understand. The data is also formatted consistently across all rows.
    *   It includes a serial number, mandatory columns, and filename, which enhances the file’s usefulness.
    *   ## !! The only reason currently uploaded excel file is showing only 7 entries because of a lack of real resume data set and not the performance issue

8. **Performance:**
     -  On average, the tool processes one resume in 7 to 12 seconds, achieving a good balance between quality and processing time.

## How to Run the Program

1.  **Clone the repository:**

    ```bash
    git clone [your_repository_link]
    cd [your_repository_name]
    ```
2.  **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create a `.env` file:**
    *   In the root directory of the project, create a file named `.env`.
    *   Add your Google Gemini API key to this file:
        ```
        GOOGLE_API_KEY="Your actual api key"
        ```
        *   **Replace `"Your actual api key"` with your actual Google Gemini API key.**
5.  **Run the Streamlit application:**
    ```bash
    streamlit run your_streamlit_app_name.py
    ```
    *   Replace `your_streamlit_app_name.py` with the name of your main Python script.

6. **Access the Web App:** Once the streamlit application is successfully launched, go to the link shown on the command line in your browser

7. **Upload PDF Resumes:** Once you are in the browser view, upload the PDF resumes that you want to analyze. You can upload single or multiple resumes at once.

8. **Analyze and Download:** Click the `Analyze` button to process your resumes. Then, use the download button to download the Excel output.

## Why Gemini Pro?

While many other models (like free hugging face models or GPT models) could be used for this task, I chose **Google Gemini Pro** for several reasons:

*   **Balance of Speed and Quality:** Gemini Pro offers a strong balance between response quality and processing time. It provided a more accurate extraction than some free and open-source alternatives.
*   **Context Handling:** Gemini Pro showed a good ability to understand and follow instructions from the prompt, extracting relevant data and adhering to the specified output format.
*   **Practical constraints:** My GPT requirements have been completed, preventing the use of any other gpt models, which I would have preffered. Additionally, the free models that I tested from hugging face (like the Flan models) had an unacceptably slow performance.

I prioritized the combination of accuracy, speed, and cost-effectiveness for this project.
## Project Structure

The main code for this project is contained in the following files:

*   **`your_streamlit_app_name.py`**: This is the main file containing the logic for the streamlit app.
*   **`requirements.txt`**: This file contains the list of packages that must be installed to run this application.
*   **`.env`**: This file will contain the google api key as mentioned above.
