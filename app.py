from flask import Flask, request, render_template, redirect, flash, session
from surveys import satisfaction_survey as survey


app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



responses = []

@app.route("/")
def home_page():
    return render_template("homepage.html", survey=survey)

@app.route("/answer", methods=["POST", "GET"])
def handle_answers():
    choice = request.form.get("form")
    responses.append(choice)
    if (len(responses) == len(survey.questions)):
        return redirect("/complete")
    else:
        return redirect(f"/question/{len(responses)}")

@app.route("/question/0")
def questions0():
    question = survey.questions[0]
    return render_template("question0.html", survey=survey, question=question)

@app.route("/question/1")
def questions1():
    question = survey.questions[1]
    if (len(responses) != 1):
        flash("go back to first question")
        redirect("/question/0")
    return render_template("question1.html", survey=survey, question=question)

@app.route("/question/2")
def questions2():
    question = survey.questions[2]
    if (len(responses) != 2):
        flash("go back to second question")
        redirect("/question/1")
    return render_template("question2.html", survey=survey, question=question)

@app.route("/question/3")
def questions3():
    question = survey.questions[3]
    if (len(responses) != 3):
        flash("go back to third question")
        redirect("/question/2")
    return render_template("question3.html", survey=survey, question=question)

@app.route("/complete")
def complete():
    responses.clear()
    return render_template("completion.html")












