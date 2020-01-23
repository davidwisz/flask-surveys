from flask import Flask, request, render_template, flash
#from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
# app.config['SECRET_KEY'] = "oh-so-secret"

# debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def display_survey():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("survey.html", title=title, instructions=instructions)

@app.route("/questions/<int:question_num>")
def display_question(question_num):
    question = satisfaction_survey.questions[question_num]
    title = f"Question {question_num + 1}"
    return render_template("survey-question.html", title=title, question=question)
    # question = satisfaction_survey.title
    # instructions = satisfaction_survey.instructions
    # return render_template("survey.html", title=title, instructions=instructions)
