from flask import Flask, render_template, request, flash, redirect, url_for, session
import smtplib
import requests
from wtforms import StringField
from wtforms.validators import DataRequired, URL
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
import os
from collections import Counter

import numpy as np

import matplotlib.pyplot as plt
from PIL import Image 

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = os.path.dirname(__file__)
app.secret_key = 'H<wK3;RA\or:9Gu96Vj_CE<$]l_K`urSyN2]S`v0E/1Z~}5qo.W0sFoc@X~I{5Q'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadimage', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as img:
                # Resize the image for faster processing if needed
                img.thumbnail((200, 200))  # Adjust the size as required

                # Get the colors from the image
                colors = img.getdata()

                # Count the occurrences of each color
                color_count = Counter(colors)

                # Get the top 10 most common colors
                session["colours"] = color_count.most_common(10)
            return redirect(url_for('result'))
    return ''

@app.route('/result', methods=['GET', 'POST'])
def result():
    some_list = session["colours"]
    return render_template("result.html")

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
