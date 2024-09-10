from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "API key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def ask_question():
    company_role = request.form['companyRole']
    company_name = request.form['companyName']
    job_description = request.form['jobDescription']
    user_resume = request.form['resume']
    question1 = request.form['question1']
    question2 = request.form['question2']
    question3 = request.form['question3']

    question = f" Act like a professional resume writer and ATS (Applicant Tracking System) optimization expert. You have 20 years of experience helping professionals across various industries create outstanding resumes that not only highlight their skills and experiences but also successfully pass ATS filters.

Objective:I am applying for {company_role}  role at {company_name}. The Job description im applying for is {job_description}. My resume is {user_resume}.. Your goal is to generate a tailored resume that:

Effectively showcases my qualifications, skills, and experiences aligned with the job description.
Optimizes keywords relevant to the role, ensuring the resume passes ATS filters.
Provides suggestions on how I can improve my resume format, content, and structure to enhance clarity, impact, and relevance.
Step-by-Step Process:
Step 1: Review the provided information including contact details, education, experience, and projects. 
Step 2: Analyze the job description to identify important keywords, skills, and qualifications required for the role. 
Step 3: Format the resume in a clean, professional style, starting with the user's contact details at the top, followed by an objective or summary that emphasizes their experience and fit for the specific role. 
Step 4: Organize the education and experience sections in reverse chronological order, incorporating the keywords identified earlier and ensuring all achievements are quantified where possible. 
Step 5: Tailor the project descriptions to highlight skills and achievements relevant to the role, embedding key phrases that align with both the job description and industry standards. 
Step 6: Suggest any improvements to sections like summary/objective, skills, and accomplishments, and provide formatting tips such as bullet points, section headers, and professional fonts to enhance readability for ATS. 
Step 7: Offer suggestions on how to further refine the resume, such as additional keywords, reducing irrelevant information, or adjusting the tone to match the job description.
Step 8: Also give me answers for {question1}, {question2}, {question3}.
Make sure the resume is comprehensive, ATS-friendly, and concise while maintaining a professional tone.

Take a deep breath and work on this problem step-by-step."

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": question}]
    )

    answer=completion.choices[0].message
    if completion.choices[0].message!=None:
        answer=completion.choices[0].message

    else :
        answer= 'Failed to Generate response!'

    
    return render_template("result.html",  answer=answer)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
