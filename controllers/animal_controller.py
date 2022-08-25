

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

@animals_blueprint.route("/animals", methods = ['POST'])
def add_the_animal():
    # animal_repository.save()
    # vets = animal_repository.vets(animal)
    return redirect("/animals")

# animals = animal_repository.select_all()


@animals_blueprint.route("/add_animal", methods=['POST'])
def create_animal():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    animal_type = request.form['animal_type']
    client_name = request.form['client_name']
    client_email = request.form['client_email']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    animal = Animal(name, date_of_birth, animal_type, client_name, client_email, treatment_notes, vet)
    animal_repository.save(animal)
    return redirect('/animals')


@animals_blueprint.route("/delete_animal")
def delete_animal():
    animals = animal_repository.select_all()
    return render_template("/animals/index.html", animal = animals)

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def remove_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')


@animals_blueprint.route("/update_animal", methods=['GET'] )
def update_the_animal():
    animals = animal_repository.select_all()
    return render_template("/animals/edit.html", animal = animals)

@animals_blueprint.route("/update_animal/<id>", methods=['PUT'])
def update_animal(id):
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    animal_type = request.form['animal_type']
    client_name = request.form['client_name']
    client_email = request.form['client_email']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    animal = Animal(name, date_of_birth, animal_type, client_name, client_email, treatment_notes, vet, id)
    animal_repository.update(animal)
    return redirect('/animals')