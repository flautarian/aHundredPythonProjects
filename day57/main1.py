from flask import Flask, render_template
import random
import datetime

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1, 10)
    year = datetime.datetime.now()
    return render_template("index.html", random_num=random_num, year=year)


if __name__ == "__main__":
    app.run(debug=True)