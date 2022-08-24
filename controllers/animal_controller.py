

from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/add_animal", )
def add_animal():
    return render_template("/animals/index.html")

@animals_blueprint.route("/animals")
def show_animal():
    animals = animal_repository.select_all()
    # vets = animal_repository.vets(animal)
    return render_template("animals/show.html", animals = animals)

# animals = animal_repository.select_all()

# @animals_blueprint.route("/animals", methods=["POST"])
# def save_animal():
#     name = request.form["name"]
#     date_of_birth = request.form["date_of_birth"]

#     animal = Animal()

@animals_blueprint.route("/add_animal", methods=['POST'])
def add_animal_to_db():
    name = request.form['animal_name']
    date_of_birth = request.form['date_of_birth']
    animal_type = request.form['animal_type']
    client_name = request.form['client_name']
    client_email = request.form['client_email']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    animal_class = Animal(name, date_of_birth, animal_type, client_name, client_email, treatment_notes, vet)
    animal_repository.save(animal_class)
    return redirect('/animals')