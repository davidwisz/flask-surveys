from flask import Flask, request, render_template, flash, redirect
import blinker
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def display_survey():

    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("survey.html", title=title, instructions=instructions)

@app.route("/questions/<int:question_num>")
def display_question(question_num):

    question_instance = satisfaction_survey.questions[question_num]
    question_text = question_instance.question
    choices = question_instance.choices
    title = f"Question {question_num + 1}"
    return render_template("survey-question.html", title=title, question=question_text, choices=choices, question_num=question_num)

@app.route("/answer", methods=["POST"])
def process_answer():

    question_num = int(request.form['question_num']) + 1
    return redirect(f"/questions/{question_num}")

