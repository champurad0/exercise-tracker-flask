from flask import render_template
from app import app


@app.route("/")
@app.route("/")
def index():
    user = {"username": "Gino"}
    workouts = [
        {
            "name": "Squat",
            "weight": "225",
            "reps": "5",
        },
        {
            "name": "Pullups",
            "weight": "0",
            "reps": "5",
        },
    ]
    return render_template("index.html", title="home", user=user, workouts=workouts)
