

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
import repositories.animal_repository as animal_repository

locations_blueprint = Blueprint("animals", __name__)

@locations_blueprint.route("/animal")
def animals():
    animals = animal_repository.select_all() # NEW
    return render_template("animals/index.html", animals = animals)

@animals_blueprint.route("/animals/<id>")
def show(id):
    animal = animal_repository.select(id)
    vets = animal_repository.vets(animal)
    return render_template("animals/show.html", animal=animal, vets=vets)