from flask import Flask, request, render_template, flash, redirect, session
import blinker
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)



@app.route("/")
def display_survey():

    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("survey.html", title=title, instructions=instructions)

@app.route("/start", methods=["POST"])
def initiate_session():
    session["responses"] = []
    return redirect("/questions/0")

@app.route("/questions/<int:question_num>")
def display_question(question_num):
    #import pdb; pdb.set_trace()
    if question_num != len(session["responses"]):
        responses = session["responses"]
        flash("You are missing an answer!")
        #breakpoint()
        return redirect(f"/questions/{len(responses)}")

    question_instance = satisfaction_survey.questions[question_num]
    question_text = question_instance.question
    choices = question_instance.choices
    title = f"Question {question_num + 1}"

    return render_template("survey-question.html", title=title, question=question_text, choices=choices, question_num=question_num)

@app.route("/answer", methods=["POST"])
def process_answer():

    question_instance = satisfaction_survey.questions
    question_num = int(request.form['question_num']) + 1

    if question_num < len(question_instance):
        responses = session["responses"]
        responses.append(request.form['question'])
        session["responses"] = responses
        destination = f"/questions/{question_num}"
    else:
        destination = "/thank-you"
    return redirect(destination)

@app.route("/thank-you")
def finish_survey():
    return render_template("thank-you.html", title="End of Survey")