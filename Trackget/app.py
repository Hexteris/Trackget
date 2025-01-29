import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import matplotlib.pyplot as plt
import io
import base64


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/trackget")
def trackget():
    # Get the user's budgeting details from sessions
    message = ''
    salary = int(session["salary"])
    saving = int(session["saving"])
    expense = int(session["expense"])

    if not (salary and saving and expense):
        return redirect("/")

    ratio = saving / salary
    percentage = ratio * 100
    yearly_saving = saving * 12

    # Create the pie chart
    chart = [saving, expense]
    labels = ['Saving', 'Expense']
    plt.figure(figsize=(5, 5))
    plt.pie(chart, labels=labels, autopct='%1.1f%%', colors=[
            'lawngreen', 'OrangeRed'], shadow=False, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the pie chart to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png', facecolor='#f0f0f0')
    img.seek(0)

    # Encode the image to base64 to embed in HTML
    img_base64 = base64.b64encode(img.getvalue()).decode('utf8')

    # Generate the linear graph
    months = list(range(1, 13))
    savings = [float(saving) * (i + 1) for i in range(12)]

    plt.figure()
    plt.plot(months, savings, marker='o')
    plt.title('Monthly Savings')
    plt.xlabel('Month')
    plt.ylabel('Savings')
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    line_graph = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template("trackget.html", yearly_saving=yearly_saving, percentage=round(percentage), salary=salary, saving=saving, expense=expense, img_base64=img_base64, line_graph=line_graph)


@app.route("/", methods=["GET", "POST"])
def info():
    if request.method == "POST":

        # Get the user's input, and store it in sessions
        session["salary"] = request.form.get("salary")
        session["saving"] = request.form.get("saving")
        session["expense"] = request.form.get("expense")
        error = None
        error2 = None
        session["trackget"] = False

        # Check if the user has inputted all of their budgeting details
        if not (session["salary"] and session["saving"] and session["expense"]):

            error = "Please input all of your budgeting details."

            return render_template("info.html", error=error)

        # Check if the user's monthly income is equal to their savings and expenses
        elif (int(session["salary"])) != (int(session["saving"]) + int(session["expense"])):

            error2 = "Your monthly income should equal your savings and expenses."

            return render_template("info.html", error2=error2)

        # if everything is correct, redirect the user to the trackget page
        else:
            session["trackget"] = True
            return redirect("/trackget")

    # if the user is just visiting the page, render the info page
    else:

        return render_template("info.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":

        return render_template("about.html")
