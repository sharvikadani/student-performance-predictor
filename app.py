from student_charts import generate_charts
from flask import Flask, render_template, request
from model import model
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/predict",
    methods=["POST"]
)

def predict():

    # Receive values from form

    hours = float(
        request.form["hours"]
    )

    attendance = float(
        request.form["attendance"]
    )

    marks = float(
        request.form["marks"]
    )

    assignments = float(
        request.form["assignments"]
    )


    # --------------------
    # Input Validation
    # --------------------

    if hours < 0 or hours > 24:

        return render_template(

            "index.html",

            error="Hours studied must be between 0 and 24"

        )


    if attendance < 0 or attendance > 100:

        return render_template(

            "index.html",

            error="Attendance must be between 0 and 100"

        )


    if marks < 0 or marks > 100:

        return render_template(

            "index.html",

            error="Marks must be between 0 and 100"

        )


    if assignments < 0 or assignments > 10:

        return render_template(

            "index.html",

            error="Assignments must be between 0 and 10"

        )



    # --------------------
    # Generate Chart
    # --------------------

    generate_charts(

        hours,
        attendance,
        marks,
        assignments

    )



    # --------------------
    # Create DataFrame
    # --------------------

    student = pd.DataFrame(

        [[

            hours,
            attendance,
            marks,
            assignments

        ]],

        columns=[

            'Hours_Studied',
            'Attendance',
            'Previous_Marks',
            'Assignments_Submitted'

        ]

    )



    # --------------------
    # Predict Grade
    # --------------------

    prediction = model.predict(
        student
    )

    grade = prediction[0]



    # --------------------
    # Grade Descriptions
    # --------------------

    description = {

        "A":"Excellent",
        "B":"Good",
        "C":"Average",
        "D":"Needs Improvement",
        "F":"Fail"

    }



    # --------------------
    # Suggestions
    # --------------------

    suggestions=[]


    if hours < 4:

        suggestions.append(
            "Study more consistently"
        )


    if attendance < 75:

        suggestions.append(
            "Improve attendance"
        )


    if marks < 60:

        suggestions.append(
            "Focus on improving marks"
        )


    if assignments < 6:

        suggestions.append(
            "Submit more assignments"
        )



    if len(suggestions)==0:

        suggestions.append(
            "Excellent performance. Keep it up!"
        )



    return render_template(

        "index.html",

        prediction=grade,

        description=description[
            grade
        ],

        suggestions=suggestions

    )


if __name__=="__main__":

    app.run(
        debug=True
    )