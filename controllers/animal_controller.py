

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
import repositories.animal_repository as animal_repository

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