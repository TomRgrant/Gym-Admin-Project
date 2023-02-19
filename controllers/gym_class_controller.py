from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint = Blueprint("gym_class", __name__)

@gym_classes_blueprint.route("/classes")
def classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/show.html", gym_classes = gym_classes)

@gym_classes_blueprint.route("/class/<id>")
def show_class_by_id(id):
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/show_id.html", gym_class = gym_class)

@gym_classes_blueprint.route("/add_new_class")
def add_new_class():
    return render_template("gym_classes/add_new_class.html")
