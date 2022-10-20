""" pet adaption app"""

from flask import Flask, request, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_db, Pet
from form import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']= 'abc123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
toolbar = DebugToolbarExtension(app)

# using function created in model connect_db 
connect_db(app)
# create database from model py
db.create_all()

@app.route('/')
def home():
    pets = Pet.query.order_by(Pet.id).all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """display list of pets and handle adding a new pets"""
    form=AddPetForm()

    if form.validate_on_submit():
        new_pet =Pet(name=form.name.data, 
                     species=form.species.data,
                     photo_url=form.photo_url.data,
                     age=form.age.data,
                     notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET","POST"])
def each_pet(pet_id):
    """display individual pet detail and handle edits to the pet info"""
    # Make a page that shows some information about the pet:

    # Name
    # Species
    # Photo, if present
    # Age, if present
    # It should also show a form that allows us to edit this pet:

    # Photo URL
    # Notes
    # Available
    # This should be at the URL /[pet-id-number]. Make the homepage link to this.
       
    pet=Pet.query.get_or_404(pet_id)
    form=EditPetForm(obj=pet)

    if form.validate_on_submit():
        
        pet.photo_url=form.photo_url.data,
        pet.notes=form.notes.data
        pet.available=form.available.data
        
        db.session.add(pet)
        db.session.commit()


        return redirect('/')

    else:
    
        return render_template('update-form.html', form=form, pet=pet)

