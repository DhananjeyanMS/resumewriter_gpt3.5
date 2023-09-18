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

    question = f"I am applying for {company_role}  role at {company_name}. You act as a professional resume writer and Tailor me my resume for the job application so that it passes through all the AI filtering mechanisms. The Job description is {job_description}. My resume is {user_resume}. Also give me answers for {question1}, {question2}, {question3}. Give me important keywords to be included in my resume with respect to the job description as well."

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
