

from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/add_animal")
def add_animal():
    vets = vet_repository.select_all()
    return render_template("/animals/new.html", vets = vets)



@animals_blueprint.route("/animals")
def show_animal():
    animals = animal_repository.select_all()
    # vets = animal_repository.vets(animal)
    return render_template("animals/show.html", animals = animals)

# animals = animal_repository.select_all()


@animals_blueprint.route("/add_animal", methods=['POST'])
def create_animal():
    name = request.form['animal_name']
    date_of_birth = request.form['date_of_birth']
    animal_type = request.form['animal_type']
    client_name = request.form['client_name']
    client_email = request.form['client_email']
    treatment_notes = request.form['treatment_notes']
    vet_id = vet_repository.select(vet_id)
    vet_id = request.form['vet_id']
    animal = Animal(name, date_of_birth, animal_type, client_name, client_email, treatment_notes)
    animal_repository.save(animal)
    return redirect('/add_animal')


@animals_blueprint.route("/delete_animal")
def delete_animal():
    animals = animal_repository.select_all()
    return render_template("/animals/index.html", animal = animals)

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def remove_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')