from flask import Flask, render_template
import random
import requests
import datetime

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/guess/<string:guess>')
def guess_person(guess):
    gender = requests.get(f"https://api.genderize.io?name={guess}").json()
    age = requests.get(f"https://api.agify.io/?name={guess}").json()
    return render_template("index.html", age=age["age"], gender=gender["gender"], name=guess)


if __name__ == "__main__":
    app.run(debug=True)