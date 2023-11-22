from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffeeshops.db'
db = SQLAlchemy()
db.init_app(app)

##CONFIGURE TABLE
class Coffeeshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    date = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    owner = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


##WTForm
class CreatecoffeeshopForm(FlaskForm):
    name = StringField("Coffee shop Name", validators=[DataRequired()])
    owner = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Shop Image URL", validators=[DataRequired(), URL()])
    description = CKEditorField("Description ", validators=[DataRequired()])
    submit = SubmitField("Submit coffee shop")


@app.route('/')
def get_all_coffeeshops():
    result = db.session.execute(db.select(Coffeeshop))
    coffeeshops = result.scalars().all()
    return render_template("index.html", all_coffeeshops=coffeeshops)


@app.route("/coffeeshop/<int:coffeeshop_id>")
def show_coffeeshop(coffeeshop_id):
    requested_coffeeshop = db.get_or_404(Coffeeshop, coffeeshop_id)
    return render_template("coffeeshop.html", coffeeshop=requested_coffeeshop)


@app.route("/new-coffeeshop", methods=["GET", "POST"])
def add_new_coffeeshop():
    form = CreatecoffeeshopForm()
    if form.validate_on_submit():
        new_coffeeshop = Coffeeshop(
            name=form.name.data,
            description=form.description.data,
            img_url=form.img_url.data,
            owner=form.owner.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_coffeeshop)
        db.session.commit()
        return redirect(url_for("get_all_coffeeshops"))
    return render_template("make-coffeeshop.html", form=form)


@app.route("/edit-coffeeshop/<int:coffeeshop_id>", methods=["GET", "POST"])
def edit_coffeeshop(coffeeshop_id):
    coffeeshop = db.get_or_404(Coffeeshop, coffeeshop_id)
    edit_form = CreatecoffeeshopForm(
        name=coffeeshop.name,
        img_url=coffeeshop.img_url,
        owner=coffeeshop.owner,
        description=coffeeshop.description
    )
    if edit_form.validate_on_submit():
        coffeeshop.name = edit_form.name.data
        coffeeshop.img_url = edit_form.img_url.data
        coffeeshop.owner = edit_form.owner.data
        coffeeshop.description = edit_form.description.data
        db.session.commit()
        return redirect(url_for("show_coffeeshop", coffeeshop_id=coffeeshop.id))
    return render_template("make-coffeeshop.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:coffeeshop_id>")
def delete_coffeeshop(coffeeshop_id):
    coffeeshop_to_delete = db.get_or_404(Coffeeshop, coffeeshop_id)
    db.session.delete(coffeeshop_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_coffeeshops'))


# Code from previous day
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
