from flask import Flask, render_template, request, session, redirect, url_for
from config import FLASK_SECRET_KEY

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/yes")
def yes():
    return render_template("yes.html")

@app.route("/next")
def next_page():
    return render_template("next.html")

@app.route("/time", methods=["GET", "POST"])
def time():
    if request.method == "POST":
        session["hour"] = request.form.get("hour")
        session["minute"] = request.form.get("minute")
        return redirect(url_for("food"))
    return render_template("time.html")

@app.route("/food")
def food():
    food_items = [
        "pizza", "sushi", "burger", "pasta",
        "salad", "indian", "waffles"
    ]
    return render_template("food.html", food_items=food_items)

@app.route("/select_food/<food>")
def select_food(food):
    session["food"] = food
    return redirect(url_for("action"))

@app.route("/action")
def action():
    action_items = [
        "film", "talk", "tablegame", "cuddle", "sex"
    ]
    return render_template("action.html", action_items=action_items)

@app.route("/select_action/<action>")
def select_action(action):
    session["action"] = action
    return redirect(url_for("final"))

@app.route("/final")
def final():
    hour = session.get("hour", "??")
    minute = session.get("minute", "??")
    food = session.get("food", "что-то вкусное")
    action = session.get("action", "что-то интересное")
    return render_template("final.html", hour=hour, minute=minute, food=food, action=action)


if __name__ == "__main__":
    app.run()