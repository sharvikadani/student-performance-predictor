import matplotlib.pyplot as plt
import os


def generate_charts(
    hours,
    attendance,
    marks,
    assignments
):

    os.makedirs(
        "static/charts",
        exist_ok=True
    )


    score = 0
    improvements=[]


    # Hours

    if hours >= 6:

        score += 25

    elif hours >=4:

        score +=18
        improvements.append(
            "Increase study hours"
        )

    elif hours >=2:

        score +=12
        improvements.append(
            "Study more consistently"
        )

    else:

        score +=5
        improvements.append(
            "Increase study hours"
        )



    # Attendance

    if attendance >=85:

        score +=25

    elif attendance >=70:

        score +=18
        improvements.append(
            "Improve attendance"
        )

    elif attendance >=50:

        score +=12
        improvements.append(
            "Attend classes regularly"
        )

    else:

        score +=5
        improvements.append(
            "Attendance needs improvement"
        )



    # Marks

    if marks >=80:

        score +=25

    elif marks >=60:

        score +=18
        improvements.append(
            "Improve marks"
        )

    elif marks >=40:

        score +=12
        improvements.append(
            "Focus on academics"
        )

    else:

        score +=5
        improvements.append(
            "Marks need improvement"
        )



    # Assignments

    if assignments >=8:

        score +=25

    elif assignments >=6:

        score +=18
        improvements.append(
            "Submit more assignments"
        )

    elif assignments >=4:

        score +=12
        improvements.append(
            "Assignment completion can improve"
        )

    else:

        score +=5
        improvements.append(
            "Complete more assignments"
        )



    remaining = 100-score



    plt.figure(
        figsize=(7,7)
    )



    plt.pie(

        [score,remaining],

        colors=[
            "#1565c0",
            "#e5edf8"
        ],

        startangle=90,

        counterclock=False,

        wedgeprops={

            "width":0.30,
            "edgecolor":"none"

        }

    )



    plt.text(

        0,
        0.10,

        f"{score}%",

        ha='center',

        fontsize=28,

        fontweight='bold'

    )



    plt.text(

        0,
        -0.08,

        "Performance",

        ha='center',

        fontsize=12,

        color='gray'

    )



    plt.savefig(

        "static/charts/heatmap.png",

        dpi=300,

        bbox_inches="tight",

        transparent=True

    )


    plt.close()