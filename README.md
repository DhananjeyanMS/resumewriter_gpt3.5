# ChatBot Project

Welcome to the Resume writer repository. This project contains a simple web-based interface built using HTML, CSS, and JavaScript, with a backend powered by Python and Flask. The webpage gets data from users on the Job they are applying for and their existing resume and generates a new resume using OpenAI's language model.

## Installation

### Prerequisites
- Python 3.7+
- Flask
- OpenAI API key


### Steps

1. Create a python flask project in your local machine
https://www.geeksforgeeks.org/flask-creating-first-simple-application/?ref=lbp

2. Download the html and python file from this repository and paste them in the respective folders in your local machine.

2. Set up environment variables:
    - Create a `.env` file in the project root directory.
    - Add your OpenAI API key:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      ```

3. Run the Flask application:
    ```sh
    python app.py
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000` to access the chatbot.

## Usage

- Open the web application in your browser.
- Enter your details in the form and "Submit".
- A new resume will be generated along with the keywords you have to embed in your resume to make your resume pass the ATS.
