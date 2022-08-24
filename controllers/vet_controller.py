
from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def show_vet():
    vets = vet_repository.select_all()
    return render_template("vets/show.html", vets = vets)


@vets_blueprint.route("/add_vet", methods = ['GET'])
def add_vet():
    vets = vet_repository.select_all()
    return render_template("/vets/new.html", vets = vets)



@vets_blueprint.route("/vets", methods=['POST'])
def create_vet():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    vet = Vet(first_name, last_name)
    vet_repository.save(vet)
    return redirect('/vets')




# @vets_blueprint.route("/vets")
# def show(id):
#     vets = vet_repository.select(id)
#     animals = animal_repository.select_all()
#     return render_template("vets/show.html", animal_list = animals)


@vets_blueprint.route("/vets", methods = ['POST'])
def vets():
    return render_template("vets/index.html")


vets = vet_repository.select_all()    

@vets_blueprint.route("/delete_vet")
def delete_vet():
    vets = vet_repository.select_all()
    return render_template("/vets/index.html", vets = vets)

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def remove_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')